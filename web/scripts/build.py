#!/usr/bin/env python3
"""MkDocs build (online u offline) o servidor de desarrollo."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

WEB_ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str], env: dict[str, str] | None = None) -> None:
    print("+", " ".join(cmd))
    subprocess.run(cmd, cwd=WEB_ROOT, check=True, env=env)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "mode",
        choices=("online", "offline", "serve"),
        help="online → site/; offline → site-offline/; serve → mkdocs serve (live reload desde 2026-china/)",
    )
    parser.add_argument(
        "--addr",
        default="0.0.0.0:8000",
        help="Dirección de mkdocs serve (default: 0.0.0.0:8000, accesible en la LAN)",
    )
    args = parser.parse_args()

    env = os.environ.copy()
    if args.mode == "serve":
        env["MKDOCS_OFFLINE"] = "false"
        run(
            [sys.executable, "-m", "mkdocs", "serve", "--dev-addr", args.addr],
            env=env,
        )
        return

    if args.mode == "offline":
        env["MKDOCS_OFFLINE"] = "true"
        site_dir = "site-offline"
    else:
        env["MKDOCS_OFFLINE"] = "false"
        site_dir = "site"

    run(
        [sys.executable, "-m", "mkdocs", "build", "--clean", "-d", site_dir],
        env=env,
    )
    print(f"OK: build {args.mode} -> web/{site_dir}/")


if __name__ == "__main__":
    main()
