#!/usr/bin/env python3
"""Verifica que los números del índice coinciden con las páginas reales."""
import re
import sys
from pathlib import Path

from pypdf import PdfReader

pdf = Path(sys.argv[1] if len(sys.argv) > 1 else "guia-indice-test2.pdf")
r = PdfReader(str(pdf))

pos: dict[str, int] = {}
for i, p in enumerate(r.pages):
    t = re.sub(r"\s+", " ", p.extract_text() or "")
    for m in re.findall(r"sec-[a-z0-9áéíóúñ-]+|day-[a-z0-9áéíóúñ-]+", t, re.I):
        pos[m.lower()] = i + 1

claves = [
    "sec-ciudades",
    "sec-pekín",
    "day-pekín-día-1-eje-imperial",
    "sec-xi-an",
]
print(f"PDF: {pdf} ({len(r.pages)} páginas)\n")
print("Posición real de marcadores:")
for k in claves:
    print(f"  {k}: pág. {pos.get(k, '?')}")

print("\nTexto del índice (págs. 3-4):")
for i in range(2, min(4, len(r.pages))):
    print(f"--- pág. {i + 1} ---")
    print(r.pages[i].extract_text() or "")
