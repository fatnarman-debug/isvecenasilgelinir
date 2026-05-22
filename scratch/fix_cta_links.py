#!/usr/bin/env python3
import os

BASE_DIR = "/Users/fatnar/Documents/isvecenasilgelinir"
blog_dir = os.path.join(BASE_DIR, "blog")

target_slugs = [
    "isvec-vatandaslik-sinavi-nedir-2026",
    "isvec-vatandaslik-sinavi-ne-zaman-agustos-2026",
    "isvec-vatandaslik-sinavi-basvurusu-ve-kayit",
    "isvec-vatandaslik-sinavi-konulari-mufredat",
    "isvec-vatandaslik-sinavi-soru-sayisi-sure-format",
    "isvec-vatandaslik-sinavi-kimler-muaf-istisnalar",
    "isvec-vatandaslik-sinavina-nasil-hazirlanilir-kaynaklar",
    "isvec-vatandaslik-sinavi-hakkinda-sikca-sorulanlar",
    "isvec-vatandaslik-sinavi-pilot-uygulama-utprovningsprov",
    "isvec-vatandaslik-sinavi-dil-ve-isvecce-seviyesi"
]

for slug in target_slugs:
    filepath = os.path.join(blog_dir, slug, "index.html")
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Check if the file contains the default iletisim link in the CTA box
    old_btn = 'href="../../iletisim/" class="btn btn-primary"'
    new_btn = 'href="https://sverigemedborgarskapsprov.com" target="_blank" rel="noopener" class="btn btn-primary"'
    
    if old_btn in content:
        content = content.replace(old_btn, new_btn)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated CTA button link in: {slug}/index.html")
    else:
        print(f"Already updated or no match in: {slug}/index.html")

print("Finished updating CTA links.")
