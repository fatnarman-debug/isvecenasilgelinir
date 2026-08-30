#!/usr/bin/env python3
"""Bozuk (placeholder) kapak gorsellerini yerel uretimle yeniden olusturur.

Her blog yazisinin HTML'inden baslik ve kategoriyi okur, assets/images
altindaki karsilik gelen PNG 2 KB'den kucukse (1x1 placeholder) yeniden uretir.

Kullanim:
  python3 scratch/backfill_covers.py --dry-run
  python3 scratch/backfill_covers.py
"""
import argparse
import glob
import html
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "agents"))
from cover_image import generate_cover  # noqa: E402

PLACEHOLDER_MAX = 2000  # bayt


def extract(path):
    s = io.open(path, encoding="utf-8").read()

    title = None
    m = re.search(r'<meta[^>]+property="og:title"[^>]+content="([^"]+)"', s)
    if not m:
        m = re.search(r'<meta[^>]+content="([^"]+)"[^>]+property="og:title"', s)
    if m:
        title = m.group(1)
    if not title:
        m = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
        if m:
            title = re.sub(r"<[^>]+>", "", m.group(1))
    if not title:
        m = re.search(r"<title>(.*?)</title>", s, re.S)
        if m:
            title = m.group(1)
    if not title:
        return None, None
    title = html.unescape(title).strip()
    title = re.split(r"\s*\|\s*", title)[0].strip()

    # Sablon kategoriyi author-meta icinde "<span>Kategori</span> • <span>Tarih</span>"
    # bicimiyle yaziyor.
    category = None
    m = re.search(r'<div class="author-meta">\s*<span>([^<]{2,60})</span>', s)
    if m:
        category = html.unescape(m.group(1)).strip()
    if not category:
        m = re.search(r'class="[^"]*category[^"]*"[^>]*>\s*([^<]{2,60})', s)
        if m:
            category = html.unescape(m.group(1)).strip()
    if not category:
        m = re.search(r'"articleSection"\s*:\s*"([^"]+)"', s)
        if m:
            category = html.unescape(m.group(1)).strip()
    return title, category or "REHBER"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    done = skipped = missing = failed = 0
    for post in sorted(glob.glob(os.path.join(ROOT, "blog", "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(post))
        img = os.path.join(ROOT, "assets", "images", slug + ".png")

        if os.path.exists(img) and os.path.getsize(img) > PLACEHOLDER_MAX:
            skipped += 1
            continue

        title, category = extract(post)
        if not title:
            print(f"[ATLA] baslik okunamadi: {slug}")
            missing += 1
            continue

        if args.dry_run:
            print(f"[KURU] {slug}\n        baslik: {title[:70]}\n        kategori: {category}")
            done += 1
        else:
            try:
                generate_cover(title, category, img)
                done += 1
                if done % 25 == 0:
                    print(f"  ... {done} gorsel uretildi")
            except Exception as e:
                print(f"[HATA] {slug}: {e}")
                failed += 1

        if args.limit and done >= args.limit:
            break

    print(f"\nuretilen: {done} | zaten saglam: {skipped} | baslik yok: {missing} | hata: {failed}")


if __name__ == "__main__":
    main()
