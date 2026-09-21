#!/usr/bin/env python3
"""Sirve la web de China 2026 con nav auto-generada (sin editar mkdocs.yml)."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
WEB_ROOT = REPO_ROOT / "web"
DOCS_DIR = REPO_ROOT / "2026-china"
BASE_CONFIG = WEB_ROOT / "mkdocs.yml"
GENERATED_CONFIG = WEB_ROOT / ".mkdocs.generated.yml"

# Orden de ciudades (ciudades.md); lo no listado va al final, alfabético.
CIUDADES_ORDEN = (
    "hong-kong",
    "pekin",
    "xian",
    "chengdu",
    "chongqing",
    "furong",
    "fenghuang",
    "guilin",
    "zhangjiajie",
    "shanghai",
)

LOGISTICA = (
    ("transportes.md", "Transportes"),
    ("alojamiento.md", "Alojamiento"),
    ("presupuesto.md", "Presupuesto"),
    ("documentacion.md", "Documentación"),
)

REFERENCIA = (
    ("consejos-locales.md", "Consejos locales"),
    ("conversion.md", "Conversión"),
)


def page_title(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            if " — " in title:
                title = title.split(" — ", 1)[0]
            return title
    return path.stem.replace("-", " ").title()


def plan_label(path: Path) -> str:
    letter = path.stem.removeprefix("plan-").upper()
    return f"Plan {letter}"


def ordered_activities(act_dir: Path) -> list[Path]:
    by_stem = {p.stem: p for p in act_dir.glob("*.md")}
    ordered: list[Path] = [by_stem[s] for s in CIUDADES_ORDEN if s in by_stem]
    rest = sorted((p for s, p in by_stem.items() if s not in CIUDADES_ORDEN), key=lambda p: p.name)
    return ordered + rest


def build_nav(docs_dir: Path) -> list:
    used: set[str] = set()
    nav: list = []

    def add(path: str, label: str, section: list | None = None) -> None:
        if not (docs_dir / path).is_file():
            return
        used.add(path)
        target = section if section is not None else nav
        target.append({label: path})

    add("index.md", "Inicio")

    reservas: list = []
    add("reservas-summary.md", "Resumen", reservas)
    add("reservas-detail.md", "Detalle", reservas)
    if reservas:
        nav.append({"Reservas": reservas})

    for plan in sorted(docs_dir.glob("plan-*.md"), key=lambda p: p.name):
        rel = plan.relative_to(docs_dir).as_posix()
        used.add(rel)
        nav.append({plan_label(plan): rel})

    add("ciudades.md", "Ciudades")

    act_dir = docs_dir / "actividades"
    if act_dir.is_dir():
        actividades: list = []
        for path in ordered_activities(act_dir):
            rel = path.relative_to(docs_dir).as_posix()
            used.add(rel)
            actividades.append({page_title(path): rel})
        if actividades:
            nav.append({"Actividades": actividades})

    logistica: list = []
    for filename, label in LOGISTICA:
        add(filename, label, logistica)
    if logistica:
        nav.append({"Logística": logistica})

    referencia: list = []
    for filename, label in REFERENCIA:
        add(filename, label, referencia)
    if referencia:
        nav.append({"Referencia": referencia})

    otros: list = []
    for path in sorted(docs_dir.rglob("*.md")):
        rel = path.relative_to(docs_dir).as_posix()
        if rel in used or rel.startswith("docs/"):
            continue
        otros.append({page_title(path): rel})
    if otros:
        nav.append({"Otros": otros})

    return nav


def format_nav_yaml(nav: list, indent: int = 0) -> list[str]:
    lines: list[str] = []
    pad = "  " * indent
    for item in nav:
        for label, value in item.items():
            if isinstance(value, str):
                lines.append(f"{pad}- {label}: {value}")
            else:
                lines.append(f"{pad}- {label}:")
                lines.extend(format_nav_yaml(value, indent + 1))
    return lines


def write_generated_config(nav: list) -> None:
    base = BASE_CONFIG.read_text(encoding="utf-8")
    header = re.sub(r"\nnav:\s*\n.*", "\n", base, flags=re.DOTALL).rstrip() + "\n"
    nav_block = "nav:\n" + "\n".join(format_nav_yaml(nav, indent=1)) + "\n"
    GENERATED_CONFIG.write_text(header + nav_block, encoding="utf-8")


def count_pages(docs_dir: Path) -> int:
    return sum(
        1
        for path in docs_dir.rglob("*.md")
        if "docs" not in path.relative_to(docs_dir).parts
    )


def serve(addr: str) -> None:
    nav = build_nav(DOCS_DIR)
    write_generated_config(nav)
    print(f"Nav auto-generada: {count_pages(DOCS_DIR)} páginas desde 2026-china/")
    print(f"Config temporal: {GENERATED_CONFIG.relative_to(REPO_ROOT)}")
    cmd = [
        sys.executable,
        "-m",
        "mkdocs",
        "serve",
        "-f",
        str(GENERATED_CONFIG),
        "--dev-addr",
        addr,
    ]
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=WEB_ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--addr",
        default="0.0.0.0:8000",
        help="Dirección de mkdocs serve (default: 0.0.0.0:8000)",
    )
    args = parser.parse_args()
    serve(args.addr)


if __name__ == "__main__":
    main()
