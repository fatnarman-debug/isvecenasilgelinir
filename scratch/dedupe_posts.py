#!/usr/bin/env python3
"""Ayni kaynak haberden uretilmis mukerrer yazilari tek yaziya indirger.

Her kumede en kapsamli yazi korunur; digerleri korunan yaziya yonlendiren
noindex + canonical + refresh saplamasina donusturulur. Liste sayfalarindaki
kartlari da kaldirir.

  python3 scratch/dedupe_posts.py --dry-run
  python3 scratch/dedupe_posts.py --apply
"""
import argparse
import collections
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "agents"))
os.environ.pop("GEMINI_API_KEY", None)
from seo_content_engine import SEOContentEngine  # noqa: E402

BASE_URL = "https://isvecenasilgelinir.com"
SOURCES = ("migrationsverket.se", "skatteverket.se", "arbetsformedlingen.se",
           "forsakringskassan.se", "pensionsmyndigheten.se", "svt.se")
LISTINGS = ["blog/index.html", "blog/sayfa-2.html", "index.html"]

STUB = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="robots" content="noindex, nofollow">
    <meta http-equiv="refresh" content="0; url={url}">
    <link rel="canonical" href="{url}">
    <title>Yönlendiriliyor...</title>
</head>
<body>
    <script>window.location.replace("{url}");</script>
</body>
</html>
"""


def is_stub(html):
    return 'http-equiv="refresh"' in html and "Yönlendiriliyor" in html


def body_words(html):
    """Yazinin govde uzunlugu. Sablon her yazida ayni oldugu icin
    karsilastirma amaciyla yeterli."""
    s = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    s = re.sub(r"<style.*?</style>", " ", s, flags=re.S | re.I)
    m = re.search(r"<h1.*?(?:</article>|<footer)", s, re.S | re.I)
    if m:
        s = m.group(0)
    return len(re.sub(r"<[^>]+>", " ", s).split())


def build_clusters():
    groups = collections.defaultdict(list)
    for path in sorted(glob.glob(os.path.join(ROOT, "blog", "*", "index.html"))):
        slug = os.path.basename(os.path.dirname(path))
        html = io.open(path, encoding="utf-8").read()
        if is_stub(html):
            continue
        for m in re.finditer(r'href="(https?://[^"]+)"', html):
            url = SEOContentEngine.normalize_url(m.group(1))
            if any(d in url for d in SOURCES):
                groups[url].append((slug, body_words(html)))
                break
    return {k: v for k, v in groups.items() if len(v) > 1}


def strip_cards(html, slugs):
    """Verilen slug'lara ait <article class="news-card"> bloklarini siler."""
    removed = 0
    out = []
    for block in re.split(r'(?=<article class="news-card">)', html):
        if block.startswith('<article class="news-card">'):
            end = block.find("</article>")
            card = block[: end + len("</article>")] if end != -1 else block
            if any(re.search(r'href="[^"]*%s/"' % re.escape(s), card) for s in slugs):
                removed += 1
                out.append(block[end + len("</article>"):] if end != -1 else "")
                continue
        out.append(block)
    return "".join(out), removed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if not (args.apply or args.dry_run):
        ap.error("--dry-run veya --apply verin")

    clusters = build_clusters()
    losers = {}
    print(f"kume: {len(clusters)}\n")
    for url, members in sorted(clusters.items(), key=lambda x: -len(x[1])):
        members.sort(key=lambda m: (-m[1], m[0]))
        keeper, kw = members[0]
        print(f"[{len(members)}] {url[:78]}")
        print(f"     TUT     {keeper}  ({kw} kelime)")
        for slug, w in members[1:]:
            print(f"     yonlen  {slug}  ({w} kelime)")
            losers[slug] = keeper
    print(f"\nkorunacak: {len(clusters)} | yonlendirilecek: {len(losers)}")

    if args.dry_run:
        return

    for slug, keeper in losers.items():
        target = f"{BASE_URL}/blog/{keeper}/"
        path = os.path.join(ROOT, "blog", slug, "index.html")
        io.open(path, "w", encoding="utf-8").write(STUB.format(url=target))
    print(f"saplama yazildi: {len(losers)}")

    for rel in LISTINGS:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        html = io.open(p, encoding="utf-8").read()
        new, removed = strip_cards(html, set(losers))
        if removed:
            io.open(p, "w", encoding="utf-8").write(new)
        print(f"{rel}: {removed} kart kaldirildi")


if __name__ == "__main__":
    main()
