"""Annotate Plan A cities as dots only (no name labels)."""
from pathlib import Path

from PIL import Image, ImageDraw

SRC = Path(r"C:\Users\santi\OneDrive\Código\Viaxes\2026-china\docs\plan-A\mapa-puntos-base.png")
OUT = Path(r"C:\Users\santi\OneDrive\Código\Viaxes\2026-china\docs\plan-A\mapa-puntos.png")

# Same approximate positions as mapa-ciudades (MapChart 1024x775)
# (name kept only for script clarity — not drawn)
PLACES = [
    ("Hong Kong", (702, 672), (0, 180, 160)),
    ("Shenzhen", (695, 652), (20, 120, 220)),
    ("Guilin", (605, 605), (0, 140, 80)),
    ("Zhangjiajie", (600, 500), (200, 40, 40)),
    ("Fenghuang", (575, 560), (180, 80, 20)),
    ("Furong", (585, 545), (160, 100, 40)),
    ("Chongqing", (525, 535), (120, 60, 180)),
    ("Chengdu", (455, 520), (0, 130, 120)),
    ("Xi'an", (545, 445), (180, 140, 0)),
    ("Pekín", (682, 298), (20, 100, 60)),
    ("Shanghái", (748, 458), (200, 40, 40)),
]


def main() -> None:
    im = Image.open(SRC).convert("RGBA")
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    r = 8
    for _, (x, y), color in PLACES:
        draw.ellipse(
            (x - r - 2, y - r - 2, x + r + 2, y + r + 2),
            fill=(255, 255, 255, 230),
        )
        draw.ellipse(
            (x - r, y - r, x + r, y + r),
            fill=color + (240,),
            outline=(30, 30, 30, 255),
            width=2,
        )

    out_im = Image.alpha_composite(im, overlay).convert("RGB")
    out_im.save(OUT, quality=95)
    print(f"saved {OUT} {out_im.size} dots={len(PLACES)}")


if __name__ == "__main__":
    main()
