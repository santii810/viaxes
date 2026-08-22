#!/usr/bin/env python3
"""Copia YYYY-destino → web/docs (sin tocar index.md)."""

from __future__ import annotations

import argparse
import os
import stat
import sys
from pathlib import Path

WEB_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = WEB_ROOT.parent
DOCS = WEB_ROOT / "docs"

SKIP_NAMES = {".DS_Store", "Thumbs.db"}


def _force_remove(path: Path) -> None:
    """Borra fichero/carpeta; tolera bloqueos típicos de OneDrive en Windows."""
    if not path.exists():
        return
    if path.is_file() or path.is_symlink():
        try:
            path.unlink()
        except PermissionError:
            os.chmod(path, stat.S_IWRITE)
            path.unlink()
        return
    for child in list(path.iterdir()):
        _force_remove(child)
    try:
        path.rmdir()
    except OSError:
        # OneDrive a veces deja el dir; se rellenará en el copy
        pass


def _copy_file(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    data = src.read_bytes()
    dst.write_bytes(data)
    try:
        os.utime(dst, (src.stat().st_atime, src.stat().st_mtime))
    except OSError:
        pass


def copy_tree(src: Path, dst: Path) -> set[Path]:
    """Copia árbol; devuelve rutas relativas escritas bajo dst."""
    written: set[Path] = set()
    if not src.exists():
        return written
    if src.is_file():
        _copy_file(src, dst)
        written.add(dst)
        return written
    for item in src.rglob("*"):
        if item.name in SKIP_NAMES or item.is_dir():
            continue
        rel = item.relative_to(src)
        target = dst / rel
        _copy_file(item, target)
        written.add(target)
    return written


def prune_extra(root: Path, keep: set[Path], preserve_names: set[str]) -> None:
    if not root.exists():
        return
    for item in sorted(root.rglob("*"), reverse=True):
        if item.is_dir():
            try:
                next(item.iterdir())
            except StopIteration:
                _force_remove(item)
            continue
        if item.name in preserve_names and item.parent == root:
            continue
        if item not in keep:
            _force_remove(item)


def sync(viaje: str) -> None:
    src = REPO_ROOT / viaje
    if not src.is_dir():
        raise SystemExit(f"No existe el viaje: {src}")

    DOCS.mkdir(parents=True, exist_ok=True)
    keep: set[Path] = set()

    for md in sorted(src.glob("*.md")):
        target = DOCS / md.name
        _copy_file(md, target)
        keep.add(target)

    keep |= copy_tree(src / "actividades", DOCS / "actividades")
    keep |= copy_tree(src / "docs", DOCS / "docs")

    prune_extra(DOCS, keep, preserve_names={"index.md"})
    print(f"OK: sincronizado {viaje} -> web/docs/")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "viaje",
        nargs="?",
        default="2026-china",
        help="Carpeta YYYY-destino (default: 2026-china)",
    )
    args = parser.parse_args()
    sync(args.viaje)


if __name__ == "__main__":
    main()
    sys.exit(0)
