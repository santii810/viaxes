"""Annotate Plan A cities on the China mapchart image."""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

SRC = Path(r"C:\Users\santi\OneDrive\Código\Viaxes\2026-china\docs\plan-A\mapa-base.png")
OUT = Path(r"C:\Users\santi\OneDrive\Código\Viaxes\2026-china\docs\plan-A\mapa-ciudades.png")


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont):
    bbox = draw.textbbox((0, 0), text, font=font)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    im = Image.open(SRC).convert("RGBA")
    _, h = im.size
    overlay = Image.new("RGBA", im.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    font = font_sm = font_title = ImageFont.load_default()
    for fp in (
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibri.ttf",
    ):
        try:
            font = ImageFont.truetype(fp, 18)
            font_sm = ImageFont.truetype(fp, 15)
            font_title = ImageFont.truetype(fp, 22)
            break
        except OSError:
            continue

    # Approximate city centers on this MapChart (1024x775)
    # Shaanxi (amarillo) ya corregido en la base → Xi'an dentro de esa provincia
    places = [
        ("Hong Kong", (702, 672), (0, 180, 160), (14, 10)),
        ("Shenzhen", (695, 652), (20, 120, 220), (14, -22)),
        ("Guilin", (605, 605), (0, 140, 80), (-95, 10)),
        ("Zhangjiajie", (600, 500), (200, 40, 40), (12, -24)),
        ("Fenghuang", (575, 560), (180, 80, 20), (-115, 8)),
        ("Furong", (585, 545), (160, 100, 40), (-100, -26)),
        ("Chongqing", (525, 535), (120, 60, 180), (14, 14)),
        ("Chengdu", (455, 520), (0, 130, 120), (-90, -10)),
        ("Xi'an", (545, 445), (180, 140, 0), (14, -10)),
        ("Pekín", (682, 298), (20, 100, 60), (14, -10)),
        ("Shanghái", (748, 458), (200, 40, 40), (14, -10)),
    ]

    for name, (x, y), color, (ldx, ldy) in places:
        r = 7
        draw.ellipse(
            (x - r, y - r, x + r, y + r),
            fill=color + (230,),
            outline=(255, 255, 255, 255),
            width=2,
        )
        lx, ly = x + ldx, y + ldy
        if abs(ldx) > 20 or abs(ldy) > 12:
            draw.line((x, y, lx, ly + 8), fill=color + (180,), width=2)
        tw, th = text_size(draw, name, font)
        pad = 4
        bx0, by0 = lx, ly
        rect = [bx0 - pad, by0 - pad, bx0 + tw + pad, by0 + th + pad]
        draw.rounded_rectangle(
            rect, radius=4, fill=(255, 255, 255, 220), outline=color + (200,), width=1
        )
        draw.text((bx0, by0), name, font=font, fill=(20, 20, 20, 255))

    title = "Plan A — ciudades en baraja"
    tw, th = text_size(draw, title, font_title)
    draw.rounded_rectangle(
        (16, 16, 16 + tw + 20, 16 + th + 16),
        radius=6,
        fill=(255, 255, 255, 230),
        outline=(40, 40, 40, 180),
        width=1,
    )
    draw.text((26, 24), title, font=font_title, fill=(20, 20, 20, 255))

    note = "Puntos ≈ ubicación ciudad (provincias coloreadas = referencia)"
    nw, _ = text_size(draw, note, font_sm)
    draw.rounded_rectangle(
        (16, h - 40, 16 + nw + 16, h - 12),
        radius=4,
        fill=(255, 255, 255, 210),
        outline=(80, 80, 80, 120),
        width=1,
    )
    draw.text((24, h - 34), note, font=font_sm, fill=(50, 50, 50, 255))

    out_im = Image.alpha_composite(im, overlay).convert("RGB")
    out_im.save(OUT, quality=95)
    print(f"saved {OUT} {out_im.size}")


if __name__ == "__main__":
    main()
