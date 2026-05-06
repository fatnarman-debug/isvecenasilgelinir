#!/usr/bin/env python3
"""
Fix all Google Search Console SEO issues:
1. Add canonical tags to all HTML files missing them
2. Update sitemap.xml with missing blog posts and remove dead URLs
3. Handle duplicate/redirect issues
"""
import os
import re
from datetime import date

BASE_DIR = "/Users/fatnar/Documents/isvecenasilgelinir"
BASE_URL = "https://isvecenasilgelinir.com"
TODAY = date.today().strftime("%Y-%m-%d")

# ─────────────────────────────────────────────
# 1. MAP: local path → canonical URL
# ─────────────────────────────────────────────
URL_MAP = {
    "index.html": f"{BASE_URL}/",
    "blog/index.html": f"{BASE_URL}/blog/",
    "hakkimizda/index.html": f"{BASE_URL}/hakkimizda/",
    "hizmetlerimiz/index.html": f"{BASE_URL}/hizmetlerimiz/",
    "hukuki-yardim/index.html": f"{BASE_URL}/hukuki-yardim/",
    "iletisim/index.html": f"{BASE_URL}/iletisim/",
}

# Auto-generate blog URL mappings from blog directories
blog_dir = os.path.join(BASE_DIR, "blog")
SKIP_DIRS = {"auto-drafts"}  # These should NOT be indexed

for entry in os.listdir(blog_dir):
    entry_path = os.path.join(blog_dir, entry)
    if os.path.isdir(entry_path) and entry not in SKIP_DIRS:
        index_file = os.path.join(entry_path, "index.html")
        if os.path.exists(index_file):
            rel_key = f"blog/{entry}/index.html"
            URL_MAP[rel_key] = f"{BASE_URL}/blog/{entry}/"

# ─────────────────────────────────────────────
# 2. ADD CANONICAL TAGS TO HTML FILES
# ─────────────────────────────────────────────
def add_canonical(filepath, canonical_url):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Skip if already has canonical
    if 'rel="canonical"' in content:
        # Update existing canonical to correct URL
        old = re.search(r'<link rel="canonical"[^>]+>', content)
        if old:
            current = old.group(0)
            if canonical_url not in current:
                new_tag = f'<link rel="canonical" href="{canonical_url}">'
                content = content.replace(current, new_tag)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  UPDATED canonical: {filepath}")
            else:
                print(f"  SKIP (already correct): {filepath}")
        return
    
    # Add canonical tag after <meta charset or first <meta
    new_tag = f'    <link rel="canonical" href="{canonical_url}">\n'
    
    # Insert after </title> or before </head> as fallback
    if '</title>' in content:
        content = content.replace('</title>', f'</title>\n{new_tag}', 1)
    elif '<meta charset' in content.lower():
        # Find the charset line and insert after it
        content = re.sub(r'(<meta charset[^>]+>)', r'\1\n' + new_tag.rstrip(), content, count=1)
    else:
        content = content.replace('</head>', f'{new_tag}</head>', 1)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ADDED canonical: {filepath}")

print("\n=== STEP 1: Adding/Fixing Canonical Tags ===")
for rel_path, canonical_url in URL_MAP.items():
    filepath = os.path.join(BASE_DIR, rel_path)
    if os.path.exists(filepath):
        add_canonical(filepath, canonical_url)
    else:
        print(f"  FILE NOT FOUND: {filepath}")

# ─────────────────────────────────────────────
# 3. FIX NOINDEX IN auto-drafts (add robots noindex)
# ─────────────────────────────────────────────
print("\n=== STEP 2: Checking auto-drafts folder ===")
auto_drafts_dir = os.path.join(BASE_DIR, "blog", "auto-drafts")
if os.path.exists(auto_drafts_dir):
    for fname in os.listdir(auto_drafts_dir):
        fpath = os.path.join(auto_drafts_dir, fname)
        if fname.endswith('.html') and os.path.isfile(fpath):
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            if 'noindex' not in content:
                # Add noindex to drafts
                noindex_tag = '    <meta name="robots" content="noindex, nofollow">\n'
                content = content.replace('</head>', f'{noindex_tag}</head>', 1)
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"  Added noindex to draft: {fname}")
            else:
                print(f"  SKIP (already noindex): {fname}")

# ─────────────────────────────────────────────
# 4. GENERATE UPDATED SITEMAP.XML
# ─────────────────────────────────────────────
print("\n=== STEP 3: Rebuilding sitemap.xml ===")

# Priority rules
def get_priority(url):
    if url == f"{BASE_URL}/":
        return "1.0"
    if "/blog/" == url[len(BASE_URL):len(BASE_URL)+6]:
        path = url[len(BASE_URL):]
        # High value blog posts
        if any(k in path for k in ["vatandaslik", "doktora-arastirmaci", "bosanma", "vergi", "maas", "is-bulma", "sirket", "hemsire", "doktor"]):
            return "0.9"
        return "0.8"
    if url == f"{BASE_URL}/blog/":
        return "0.9"
    return "0.8"

# Date map for known posts (don't backdate new ones)
DATE_MAP = {
    f"{BASE_URL}/": "2026-05-06",
    f"{BASE_URL}/blog/": "2026-05-06",
    f"{BASE_URL}/blog/isvec-vatandaslik-yeni-kurallar-2026/": "2026-05-06",
    f"{BASE_URL}/blog/isvecte-doktora-arastirmaci-yeni-kurallar-2026/": "2026-05-05",
    f"{BASE_URL}/blog/isvecte-bosanma-tanima-tenfiz-rehberi/": "2026-05-06",
    f"{BASE_URL}/blog/isvecte-bosanan-kadinlar-mal-paylasimi-rehberi/": "2026-05-06",
    f"{BASE_URL}/blog/isvecte-sirket-acmak-rehberi-2026/": "2026-05-04",
}

# Collect all valid URLs
sitemap_urls = []

# Homepage
sitemap_urls.append((f"{BASE_URL}/", "1.0", "2026-05-06"))

# Blog listing page
sitemap_urls.append((f"{BASE_URL}/blog/", "0.9", "2026-05-06"))

# Static pages
for page in ["hakkimizda", "hizmetlerimiz", "hukuki-yardim", "iletisim"]:
    page_path = os.path.join(BASE_DIR, page, "index.html")
    if os.path.exists(page_path):
        sitemap_urls.append((f"{BASE_URL}/{page}/", "0.7", "2026-05-01"))

# Blog posts (exclude auto-drafts and duplicates)
EXCLUDE_BLOGS = {"auto-drafts", "isvecte-vergi-sistemi-2026"}  # isvecte-vergi-sistemi-2026 is duplicate of rehberi-2026

blog_posts = []
for entry in sorted(os.listdir(blog_dir)):
    entry_path = os.path.join(blog_dir, entry)
    index_path = os.path.join(entry_path, "index.html")
    if os.path.isdir(entry_path) and entry not in EXCLUDE_BLOGS and os.path.exists(index_path):
        url = f"{BASE_URL}/blog/{entry}/"
        last_mod = DATE_MAP.get(url, "2026-05-01")
        priority = get_priority(url)
        blog_posts.append((url, priority, last_mod))

# Sort by date descending (newest first)
blog_posts.sort(key=lambda x: x[2], reverse=True)
sitemap_urls.extend(blog_posts)

# Generate XML
xml_lines = ['<?xml version="1.0" encoding="UTF-8"?>']
xml_lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for url, priority, lastmod in sitemap_urls:
    xml_lines.append('    <url>')
    xml_lines.append(f'        <loc>{url}</loc>')
    xml_lines.append(f'        <lastmod>{lastmod}</lastmod>')
    xml_lines.append(f'        <priority>{priority}</priority>')
    xml_lines.append('    </url>')

xml_lines.append('</urlset>')

sitemap_content = '\n'.join(xml_lines) + '\n'
sitemap_path = os.path.join(BASE_DIR, "sitemap.xml")
with open(sitemap_path, 'w', encoding='utf-8') as f:
    f.write(sitemap_content)

print(f"  Sitemap rebuilt with {len(sitemap_urls)} URLs")
print(f"  Saved to: {sitemap_path}")

# ─────────────────────────────────────────────
# 5. ADD REDIRECT for duplicate isvecte-vergi-sistemi-2026
# ─────────────────────────────────────────────
print("\n=== STEP 4: Adding redirect for duplicate blog ===")
dup_dir = os.path.join(BASE_DIR, "blog", "isvecte-vergi-sistemi-2026")
if os.path.exists(dup_dir):
    redirect_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="robots" content="noindex, nofollow">
    <meta http-equiv="refresh" content="0; url=https://isvecenasilgelinir.com/blog/isvecte-vergi-sistemi-rehberi-2026/">
    <link rel="canonical" href="https://isvecenasilgelinir.com/blog/isvecte-vergi-sistemi-rehberi-2026/">
    <title>Yönlendiriliyor...</title>
</head>
<body>
    <script>window.location.replace("https://isvecenasilgelinir.com/blog/isvecte-vergi-sistemi-rehberi-2026/");</script>
</body>
</html>"""
    dup_index = os.path.join(dup_dir, "index.html")
    with open(dup_index, 'w', encoding='utf-8') as f:
        f.write(redirect_html)
    print(f"  Redirect added: isvecte-vergi-sistemi-2026 → isvecte-vergi-sistemi-rehberi-2026")

print("\n✅ All SEO fixes complete!")
print("\nSummary:")
print(f"  - Canonical tags added/fixed: {len(URL_MAP)} files")
print(f"  - Sitemap rebuilt: {len(sitemap_urls)} valid URLs")
print(f"  - Duplicate redirect: isvecte-vergi-sistemi-2026 fixed")
print(f"  - auto-drafts: noindex protected")
