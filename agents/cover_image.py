#!/usr/bin/env python3
"""Marka kimligine uygun blog kapak gorseli uretir (1200x630, OG boyutu).

Tamamen yerel calisir: API cagrisi, kota ve ag bagimliligi yoktur.
Tipografi sitenin Inter ailesiyle ayni; renkler ana sayfadaki
lacivert/mavi paletinden turetilmistir.
"""
import hashlib
import os
import re
import unicodedata

from PIL import Image, ImageDraw, ImageFont

W, H = 1200, 630

# Site paletinden turetilen zemin tonlari (index.html: #005bb5 / #003f82 / #0f172a)
BG_DEEP = (10, 37, 64)        # derin lacivert
BG_ARC = (14, 50, 87)         # zeminden bir ton acik yay
HAIRLINE = (0, 91, 181)       # marka mavisi ince cizgi
TITLE_COLOR = (255, 255, 255)
FOOTER_COLOR = (143, 169, 196)

# Lacivert zeminde AA kontrasti saglayan aksan tonlari.
# Kategori adindan deterministik secilir: ayni kategori hep ayni rengi alir.
ACCENTS = [
    (233, 180, 76),   # altin
    (86, 184, 168),   # cam yesili
    (226, 123, 95),   # kiremit
    (196, 173, 232),  # lavanta
]

FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "fonts")

# Yerlesim: sol sutun genis, sag bosluk daha genis birakilir.
# Bilincli asimetri; ortalanmis "sablon" gorunumunden kacinir.
MARGIN_L = 88
COL_W = 780
# Metin blogu su bandin icine optik olarak ortalanir; boylece 1 satirlik da
# 3 satirlik da baslik ayni dengede durur.
BAND_TOP, BAND_BOTTOM = 132, 508
RULE_W, RULE_H = 56, 5
CAT_GAP = 30
TITLE_GAP = 34
FOOTER_Y = H - 96

TR_UPPER = str.maketrans({"i": "İ", "ı": "I"})


def _font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def tr_upper(s):
    """Turkce'ye uygun buyuk harf: i->İ, ı->I."""
    return s.translate(TR_UPPER).upper()


def accent_for(category):
    h = hashlib.md5((category or "").strip().lower().encode("utf-8")).hexdigest()
    return ACCENTS[int(h, 16) % len(ACCENTS)]


def _text_w(draw, text, font, tracking=0):
    w = draw.textlength(text, font=font)
    return w + tracking * max(len(text) - 1, 0)


def _draw_tracked(draw, xy, text, font, fill, tracking):
    """Harf araligi vererek yazar (Pillow'da yerlesik tracking yok)."""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=font, fill=fill)
        x += draw.textlength(ch, font=font) + tracking


def _wrap(draw, text, font, max_w):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if draw.textlength(trial, font=font) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines


def _fit_title(draw, title, max_w, max_lines=3, start=64, min_size=38):
    """Basligi max_lines satira sigana kadar kuculterek en iyi boyutu bulur."""
    size = start
    while size >= min_size:
        font = _font("Inter-Bold.ttf", size)
        lines = _wrap(draw, title, font, max_w)
        if len(lines) <= max_lines:
            return font, lines, size
        size -= 2
    font = _font("Inter-Bold.ttf", min_size)
    lines = _wrap(draw, title, font, max_w)[:max_lines]
    if lines:
        lines[-1] = lines[-1].rstrip(" ,.;:") + "…"
    return font, lines, min_size


def _background(accent):
    """Zemin: dikey olarak hafif koyulasan lacivert; sag kenardan tasan
    ic ice iki halka ve ust kenarda ince marka cizgisi.

    Halkalarin merkezi bilerek kadraj disinda birakilir: kompozisyon
    ortalanmis bir sablon gibi degil, sag bosluga dayanmis gibi okunur.
    """
    img = Image.new("RGB", (W, H), BG_DEEP)
    d = ImageDraw.Draw(img)

    # Duz dolgunun matligini kiran cok hafif dikey koyulasma.
    for i in range(H):
        a = int((i / H) ** 1.6 * 16)
        d.line([(0, i), (W, i)], fill=(max(BG_DEEP[0] - a, 0),
                                       max(BG_DEEP[1] - a, 0),
                                       max(BG_DEEP[2] - a, 0)))

    overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    cx, cy = W - 40, 300          # merkez kadrajin sag disinda
    od.ellipse([cx - 330, cy - 330, cx + 330, cy + 330], fill=BG_ARC + (170,))
    od.ellipse([cx - 250, cy - 250, cx + 250, cy + 250],
               outline=BG_ARC + (255,), width=2)
    od.ellipse([cx - 430, cy - 430, cx + 430, cy + 430],
               outline=BG_ARC + (130,), width=2)
    # Halkalari kesen kisa aksan yayi: gozu sag ust bosluga baglar.
    od.arc([cx - 330, cy - 330, cx + 330, cy + 330], 196, 232,
           fill=accent + (190,), width=4)
    img = Image.alpha_composite(img.convert("RGBA"), overlay).convert("RGB")

    d = ImageDraw.Draw(img)
    d.rectangle([0, 0, W, 6], fill=HAIRLINE)
    d.rectangle([0, 0, 210, 6], fill=accent)
    return img


def generate_cover(title, category, out_path, site="isvecenasilgelinir.com"):
    """Kapak gorselini uretip PNG olarak kaydeder."""
    accent = accent_for(category)
    img = _background(accent)
    d = ImageDraw.Draw(img)

    cat = tr_upper((category or "REHBER").replace("&amp;", "&").strip())
    cat_font = _font("Inter-SemiBold.ttf", 21)
    title_font, lines, size = _fit_title(d, title.strip(), COL_W)
    leading = int(size * 1.18)

    # Blok yuksekligini olcup banda ortala
    block_h = RULE_H + CAT_GAP + 21 + TITLE_GAP + len(lines) * leading
    top = BAND_TOP + max((BAND_BOTTOM - BAND_TOP) - block_h, 0) // 2

    d.rectangle([MARGIN_L, top, MARGIN_L + RULE_W, top + RULE_H], fill=accent)

    cat_y = top + RULE_H + CAT_GAP
    _draw_tracked(d, (MARGIN_L, cat_y), cat, cat_font, accent, 2.4)

    y = cat_y + 21 + TITLE_GAP
    for ln in lines:
        d.text((MARGIN_L, y), ln, font=title_font, fill=TITLE_COLOR)
        y += leading

    # Alt bilgi: aksan noktasi + alan adi
    foot_font = _font("Inter-Medium.ttf", 21) if os.path.exists(
        os.path.join(FONT_DIR, "Inter-Medium.ttf")) else _font("Inter-Regular.ttf", 21)
    d.ellipse([MARGIN_L, FOOTER_Y + 6, MARGIN_L + 9, FOOTER_Y + 15], fill=accent)
    d.text((MARGIN_L + 22, FOOTER_Y), site, font=foot_font, fill=FOOTER_COLOR)

    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    img.save(out_path, "PNG", optimize=True)
    return out_path


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 4:
        print("kullanim: cover_image.py <baslik> <kategori> <cikti.png>")
        sys.exit(1)
    print(generate_cover(sys.argv[1], sys.argv[2], sys.argv[3]))
