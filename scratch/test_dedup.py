#!/usr/bin/env python3
"""Mukerrer tespitinin kaynak URL uzerinden calistigini dogrular."""
import os, sys
sys.path.insert(0, os.path.join(os.getcwd(), 'agents'))
os.environ.pop('GEMINI_API_KEY', None)
from seo_content_engine import SEOContentEngine

SV_LINK = ("https://www.migrationsverket.se/nyhetsarkiv/nyhetsarkiv/"
           "2026-08-27-ulrika-karlsson-ny-presschef-pa-migrationsverket.html")
SV_TITLE = "Ulrika Karlsson ny press­chef på Migra­tions­verket"
FRESH_LINK = "https://www.skatteverket.se/nyheter/nu-kontrolleras-landets-byggen-2026.html"

e = SEOContentEngine(".")
ok = True

if not hasattr(e, "load_published_sources"):
    print("FAIL: load_published_sources yok"); sys.exit(1)

pub = e.load_published_sources()
print(f"toplanan kaynak URL sayisi: {len(pub)}")

if e.is_source_published(SV_LINK, pub):
    print("PASS: yayinlanmis kaynak mukerrer olarak tespit edildi")
else:
    print("FAIL: yayinlanmis kaynak tespit EDILEMEDI"); ok = False

if not e.is_source_published(FRESH_LINK, pub):
    print("PASS: yeni kaynak yanlislikla mukerrer sayilmadi")
else:
    print("FAIL: yeni kaynak yanlislikla mukerrer sayildi"); ok = False

sys.exit(0 if ok else 1)
