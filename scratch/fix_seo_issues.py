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

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
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
    f"{BASE_URL}/blog/isvec-eu-tarim-ilaci-kurallari-saglik-cevreyi-tehdit-ediyor/": "2026-07-06",
    f"{BASE_URL}/blog/isvec-yeni-vab-haklari-okul-toplantilari/": "2026-07-06",
    f"{BASE_URL}/blog/isvec-sosyal-sigorta-degisiklikleri-2026/": "2026-07-06",
    f"{BASE_URL}/blog/isvec-dijital-miras-envanteri-bouppteckning-2026-ilk-adim/": "2026-07-06",
    f"{BASE_URL}/blog/isvec-vab-haklari-yeni-duzenlemeler-2026/": "2026-07-05",
    f"{BASE_URL}/blog/isvec-sosyal-guvenlik-yasalarinda-guncellemeler-2026/": "2026-07-05",
    f"{BASE_URL}/blog/isvec-dijital-bouppteckning-ilk-adim/": "2026-07-05",
    f"{BASE_URL}/blog/isvec-tecavuz-sucuna-multeci-sinirdisi-kurallari-degisti/": "2026-07-04",
    f"{BASE_URL}/blog/isvec-vab-haklari-genisledi-okul-toplantilari-icin-yeni-imkanlar/": "2026-07-04",
    f"{BASE_URL}/blog/isvec-sosyal-guvenlik-yasasi-degisiklikleri-2026/": "2026-07-04",
    f"{BASE_URL}/blog/isvec-dijital-miras-envanteri-ilk-adim/": "2026-07-04",
    f"{BASE_URL}/blog/isvec-sl-toplu-tasima-aksakliklari-temmuz-2026/": "2026-07-03",
    f"{BASE_URL}/blog/lag-degisiklikleri-isvec-sosyal-guvenlik-2026-temmuz/": "2026-07-03",
    f"{BASE_URL}/blog/isvec-dijital-envanter-belgesi-donemi-basliyor-skatteverket-2027/": "2026-07-03",
    f"{BASE_URL}/blog/vasteras-cinayeti-karisini-olduren-adama-omur-boyu-hapis-cezasi/": "2026-07-02",
    f"{BASE_URL}/blog/isvec-vab-yeni-kurallar-2026-okul-toplantilari/": "2026-07-02",
    f"{BASE_URL}/blog/isvecte-sosyal-sigorta-sisteminde-yeni-duzenlemeler-2026/": "2026-07-02",
    f"{BASE_URL}/blog/isvec-dijital-miras-beyannamesi-yeni-yasa-2026/": "2026-07-02",
    f"{BASE_URL}/blog/eski-fra-calisani-hakkindaki-sorusturma-dustu-isvec-guvenligi/": "2026-07-01",
    f"{BASE_URL}/blog/isvec-yeni-vab-haklari-okul-toplantilari-sosyal-hizmetler-2026/": "2026-07-01",
    f"{BASE_URL}/blog/isvec-sosyal-guvenlik-yasalarinda-1-temmuz-2026-degisiklikleri/": "2026-07-01",
    f"{BASE_URL}/blog/isvec-dijital-miras-envanteri/": "2026-07-01",
    f"{BASE_URL}/blog/jonas-falk-yeniden-yargilaniyor-isvecin-en-buyuk-narkotik-davasi/": "2026-06-30",
    f"{BASE_URL}/blog/isvec-yaz-aylarinda-yaralanmalar-ve-hastalik-odenegi/": "2026-06-30",
    f"{BASE_URL}/blog/isvec-yeni-vab-okul-sosyal-hizmetler-toplantilari/": "2026-06-30",
    f"{BASE_URL}/blog/isvec-isizlik-tahmini-2026-2027-bolgesel-perspektif/": "2026-06-30",
    f"{BASE_URL}/blog/isvec-dijital-miras-envanteri-2027/": "2026-06-30",
    f"{BASE_URL}/blog/isvec-yaz-aylarinda-artan-yaralanmalar/": "2026-06-29",
    f"{BASE_URL}/blog/isvec-kripto-madencilik-vergi-denetimleri-skatteverket-2026/": "2026-06-29",
    f"{BASE_URL}/blog/isvec-goc-idarasi-siginma-istatistikleri-kisitlamasi/": "2026-06-29",
    f"{BASE_URL}/blog/isvec-hassas-bolgelerde-isvecce-dil-destegi/": "2026-06-28",
    f"{BASE_URL}/blog/isvec-iskur-issizlik-prognozu-2026-2027/": "2026-06-28",
    f"{BASE_URL}/blog/isvec-kripto-madencilik-vergi-denetimleri-2026/": "2026-06-28",
    f"{BASE_URL}/blog/migrationsverkets-almedalsveckan-2026-katilimi/": "2026-06-28",
    f"{BASE_URL}/blog/isvec-iltica-uluslararasi-koruma-istatistikleri-gecici-kisitlama/": "2026-06-28",
    f"{BASE_URL}/blog/isvec-issizlik-tahmini-2026-2027-bolgesel/": "2026-06-27",
    f"{BASE_URL}/blog/isvec-iltica-ve-siginma-istatistikleri-gecici-kisitlama-2026/": "2026-06-27",
    f"{BASE_URL}/blog/isvec-bolgesel-issizlik-tahmini-2026-2027/": "2026-06-26",
    f"{BASE_URL}/blog/isvec-kripto-madenciligi-sektorunde-vergi-denetimleri-2026/": "2026-06-26",
    f"{BASE_URL}/blog/isvec-migrationsverket-almedalen-haftasi-2026-katilimi/": "2026-06-26",
    f"{BASE_URL}/blog/isvec-iltica-ve-koruma-istatistikleri-gecici-kisitlama-2026/": "2026-06-26",
    f"{BASE_URL}/blog/isvec-islizlik-oranlari-2026-bolgesel-analiz/": "2026-06-25",
    f"{BASE_URL}/blog/skatteverket-nufus-verileri-kayit-dogrulugu-2026/": "2026-06-25",
    f"{BASE_URL}/blog/isvec-kripto-madencilik-vergi-denetimleri-2026/": "2026-06-25",
    f"{BASE_URL}/blog/migrationsverkets-almedalsveckan-2026-katilim-detaylari/": "2026-06-25",
    f"{BASE_URL}/blog/isvec-nufus-durumu-2026-skatteverket-raporu/": "2026-06-23",
    f"{BASE_URL}/blog/isvec-cocuklu-ailelerin-ekonomik-durumu-2026/": "2026-06-22",
    f"{BASE_URL}/blog/isvec-is-bulma-destekleri-2026-arbetsformedlingen-raporu/": "2026-06-22",
    f"{BASE_URL}/blog/isvec-nufus-kayitlarindaki-son-durum-skatteverket-2026-raporu/": "2026-06-22",
    f"{BASE_URL}/blog/isvec-kripto-madencilik-vergi-cezalari-skatteverket-2026/": "2026-06-22",
    f"{BASE_URL}/blog/migrationsverket-almedalsveckan-2026-goc-toplum-gelisimi/": "2026-06-22",
    f"{BASE_URL}/blog/isvec-goc-istatistikleri-gecici-kisitlama-eu-yeni-kurallar/": "2026-06-22",
    f"{BASE_URL}/blog/isvec-issizlikle-mucadelede-en-etkili-yontemler/": "2026-06-21",
    f"{BASE_URL}/blog/isvec-nufus-raporu-skatteverket-2026/": "2026-06-21",
    f"{BASE_URL}/blog/migrationsverket-yeni-hanedan-armasi-logo/": "2026-06-21",
    f"{BASE_URL}/blog/isvec-iskandinav-adalet-sistemi-oslo-suc-davasi/": "2026-06-20",
    f"{BASE_URL}/blog/isvec-yabanci-kokenli-ailelerin-ekonomik-durumunda-iyilesme-forsakringskassan-2026/": "2026-06-20",
    f"{BASE_URL}/blog/isvec-issizlik-pazari-2026-2027-tahminleri/": "2026-06-20",
    f"{BASE_URL}/blog/isvec-issizlikle-mucadele-raporu-2026/": "2026-06-20",
    f"{BASE_URL}/blog/isvec-nufus-kayitlari-skatteverket-2026-raporu/": "2026-06-20",
    f"{BASE_URL}/blog/migrationsverket-yeni-logo-armali-tasarim/": "2026-06-20",
    f"{BASE_URL}/blog/isvec-gocmen-ailelerin-ekonomik-durumu-iyilesiyor-2026/": "2026-06-19",
    f"{BASE_URL}/blog/isvec-issizlik-beklentileri-2026-2027/": "2026-06-19",
    f"{BASE_URL}/blog/isvec-is-piyasasi-raporu-issizlere-en-iyi-sonuclari-veren-stratejiler/": "2026-06-19",
    f"{BASE_URL}/blog/skatteverket-isvec-nufus-raporu-2026/": "2026-06-19",
    f"{BASE_URL}/blog/ab-ortak-goc-iltica-kurallari-isvec/": "2026-06-19",
    f"{BASE_URL}/blog/migrationsverket-yeni-logosu-heraldik-arma-2026/": "2026-06-19",
    f"{BASE_URL}/blog/isvec-midsommar-hava-durumu-2026-yagmur-uyarisi/": "2026-06-18",
    f"{BASE_URL}/blog/isvec-babalar-futbol-ebeveyn-izni-miti-forsakringskassan/": "2026-06-18",
    f"{BASE_URL}/blog/isvece-gocmen-ailerinin-ekonomik-durumu-gelisiyor-2026-forsakringskassan-raporu/": "2026-06-18",
    f"{BASE_URL}/blog/isvec-issizlik-beklentileri-2026-2027/": "2026-06-18",
    f"{BASE_URL}/blog/isvec-issizlere-is-bulma-rehberi-arbetsformedlingen-raporu-2026/": "2026-06-18",
    f"{BASE_URL}/blog/skatteverket-isvec-nufus-durum-raporu-2026/": "2026-06-18",
    f"{BASE_URL}/blog/ab-goc-ve-iltica-pakti-isvec/": "2026-06-18",
    f"{BASE_URL}/blog/migrationsverket-yeni-logo-milli-arma/": "2026-06-18",
    f"{BASE_URL}/blog/isvec-ekonomi-haziran-2026-prognozlar/": "2026-06-17",
    f"{BASE_URL}/blog/isvec-yabanci-kokenli-ailelerin-ekonomik-durumu-gelisiyor/": "2026-06-17",
    f"{BASE_URL}/blog/isvec-mayis-2026-issizlik-verileri-en-dusuk-seviye/": "2026-06-17",
    f"{BASE_URL}/blog/isvec-issizlik-beklentileri-2026-2027-arbetsformedlingen-raporu/": "2026-06-17",
    f"{BASE_URL}/blog/ab-goc-iltica-pakti-isvec-2026/": "2026-06-17",
    f"{BASE_URL}/blog/migrationsverket-yeni-logo-heraldik-armasi/": "2026-06-17",
    f"{BASE_URL}/blog/isvec-liberal-parti-yeni-secim-stratejisi-livspusselfeminism/": "2026-06-16",
    f"{BASE_URL}/blog/onumuzdeki-iki-yilda-isvec-issizlik-tahminleri/": "2026-06-16",
    f"{BASE_URL}/blog/migrationsverket-yeni-hanedan-armali-logo-detayli-rehber/": "2026-06-16",
    f"{BASE_URL}/blog/isvec-sosyal-sigorta-harcamalari-1980den-bu-yana-en-dusuk-seviyede/": "2026-06-15",
    f"{BASE_URL}/blog/isvec-babalar-ebeveyn-izni-futbol-efsanesi/": "2026-06-15",
    f"{BASE_URL}/blog/isvec-issizlik-rakamlari-mayis-2026/": "2026-06-15",
    f"{BASE_URL}/blog/isvec-2026-vergi-iadesi-ve-kvarskatt-duyurusu/": "2026-06-15",
    f"{BASE_URL}/blog/isvec-gocmenlik-vize-egitim-calisma-yeni-kurallar-haziran-2026/": "2026-06-15",
    f"{BASE_URL}/blog/isvec-eu-goc-iltica-pakti-2026/": "2026-06-15",
    f"{BASE_URL}/blog/isvec-issizlik-orani-mayis-2026-analizi/": "2026-06-14",
    f"{BASE_URL}/blog/isvec-vergi-iadesi-2026-skatteverket-duyurdu/": "2026-06-14",
    f"{BASE_URL}/blog/isvecte-yeni-gocmenlik-kurallari-2026/": "2026-06-14",
    f"{BASE_URL}/blog/eu-ortak-goc-iltica-kurallari-isvec/": "2026-06-14",
    f"{BASE_URL}/blog/isvec-kraliyet-cifti-altin-evlilik-yildonumu-kutlamalari-2026/": "2026-06-13",
    f"{BASE_URL}/blog/isvec-sosyal-guvenlik-harcamalari-1980den-bu-yana-en-dusuk-seviyede-2026/": "2026-06-13",
    f"{BASE_URL}/blog/isvec-vergi-iadesi-2026-skatteverket-duyurdu/": "2026-06-13",
    f"{BASE_URL}/blog/isvec-yeni-gocmenlik-kurallari-ogrenci-arastirmaci-gecici-koruma/": "2026-06-13",
    f"{BASE_URL}/blog/ab-ortak-goc-iltica-kurallari-yururlukte/": "2026-06-13",
    f"{BASE_URL}/blog/isvec-guvenligi-rusya-nato-testi-savunma-raporu-2026/": "2026-06-12",
    f"{BASE_URL}/blog/isvec-sosyal-sigorta-giderleri-tarihi-dususte-2025/": "2026-06-12",
    f"{BASE_URL}/blog/isvecte-babalarin-dogum-izni-ve-spor-turnuvalari-efsanesi/": "2026-06-12",
    f"{BASE_URL}/blog/isvec-mayis-2026-issizlik-rakamlari/": "2026-06-12",
    f"{BASE_URL}/blog/isvec-vergi-iadesi-2026-haziran-skatteverket/": "2026-06-12",
    f"{BASE_URL}/blog/isvec-gocmenlik-yeni-kurallar-haziran-2026/": "2026-06-12",
    f"{BASE_URL}/blog/eu-goc-ve-iltica-pakti-isvec-2026/": "2026-06-12",
    f"{BASE_URL}/blog/isvec-babalar-ebeveyn-izni-futbol-vm-efsanesi/": "2026-06-11",
    f"{BASE_URL}/blog/isvec-mayis-2026-issizlik-rakamlari-ve-istihdam-pazari-analizi/": "2026-06-11",
    f"{BASE_URL}/blog/iskec-pazar-ve-sokak-ticareti-vergi-denetimleri-2026/": "2026-06-11",
    f"{BASE_URL}/blog/isvec-vergi-iadesi-2026-haziran/": "2026-06-11",
    f"{BASE_URL}/blog/isvec-iran-lubnan-siginma-basvurusu-paus-2026/": "2026-06-11",
    f"{BASE_URL}/blog/isvec-sosyal-guvenlik-harcamalari-1980den-bu-yana-en-dusuk-seviyede/": "2026-06-10",
    f"{BASE_URL}/blog/skatteverket-pazar-piyasa-denetimleri-2026/": "2026-06-10",
    f"{BASE_URL}/blog/isvec-vergi-iadesi-2026-skatteverket-duyurusu/": "2026-06-10",
    f"{BASE_URL}/blog/isvec-anayasa-komisyonu-ku-hukumet-denetiminde-bolunme/": "2026-06-09",
    f"{BASE_URL}/blog/isvec-sosyal-guvenlik-harcamalari-son-45-yilin-en-dusuk-seviyesi/": "2026-06-09",
    f"{BASE_URL}/blog/isvec-vergi-iadesi-2026-skatteverket-duyurdu/": "2026-06-09",
    f"{BASE_URL}/blog/isvec-genc-yetiskin-oturma-izni-duzenlemesi/": "2026-06-09",
    f"{BASE_URL}/blog/sd-faktura-skandali-jimmie-festeri-vergi-kacirma-iddialari/": "2026-06-08",
    f"{BASE_URL}/blog/isvec-yurtdisi-saglik-eu-kortet-forsakringskassan-uyanigi/": "2026-06-08",
    f"{BASE_URL}/blog/isvecte-pazar-sokak-ticaretine-skatteverketten-siki-kontrol/": "2026-06-08",
    f"{BASE_URL}/blog/isvec-vergi-iadesi-2026-haziran-odeme-detaylari/": "2026-06-08",
    f"{BASE_URL}/blog/isvec-guvenlik-tehditlerinin-haklari-kisitlandi-2026/": "2026-06-08",
    f"{BASE_URL}/blog/isvec-genc-yetiskin-oturma-izni-duzenlemesi-2026/": "2026-06-08",
    f"{BASE_URL}/blog/isvec-eu-saglik-sigortasi-karti-unutmayin/": "2026-06-06",
    f"{BASE_URL}/blog/isvecte-dijital-hindersprovning-yaz-dugunleri/": "2026-06-06",
    f"{BASE_URL}/blog/isvec-pazar-esnafi-vergi-kontrolleri-2026/": "2026-06-06",
    f"{BASE_URL}/blog/isvec-guvenlik-tehditleri-icin-yeni-sinirdisi-kurallari-2026/": "2026-06-06",
    f"{BASE_URL}/blog/isvec-goc-idaresi-gencler-icin-yeni-yasa-teklifi-sonrasi-sinirdisi-islemlerini-durdurdu/": "2026-06-06",
    f"{BASE_URL}/blog/isvec-trafik-idaresi-tasarruf-uyari-2026/": "2026-06-05",
    f"{BASE_URL}/blog/isvecte-dijital-evlilik-engel-kontrolu-2026/": "2026-06-05",
    f"{BASE_URL}/blog/isvec-pazar-ve-sokak-ticareti-denetimleri-2026/": "2026-06-05",
    f"{BASE_URL}/blog/isvec-guvenlik-tehditleri-icin-yeni-hak-kisitlamalari/": "2026-06-05",
    f"{BASE_URL}/blog/isvec-genc-yetiskin-oturma-izni-yeni-duzenleme-2026/": "2026-06-05",
    f"{BASE_URL}/blog/yurtdisinda-hastalanmak-ab-saglik-sigortasi-karti/": "2026-06-04",
    f"{BASE_URL}/blog/isvecte-gencler-icin-sinirdisi-durdurma-karari-2026/": "2026-06-02",
    f"{BASE_URL}/blog/isvecte-genc-siginmacilara-oturum-izni-kolayligi-2026/": "2026-06-01",
    f"{BASE_URL}/blog/isvec-premiepension-emeklilik-fonlari-rehberi/": "2026-05-26",
    f"{BASE_URL}/blog/isvecte-turkce-avukat-ve-hukuki-yardim-rehberi/": "2026-05-24",
    f"{BASE_URL}/blog/isvecte-calisma-izni-maas-siniri-muaf-meslekler-2026/": "2026-05-24",
    f"{BASE_URL}/blog/isvec-vatandaslik-sartlari-2026/": "2026-05-23",
    f"{BASE_URL}/blog/isvec-vatandaslik-basvurusu/": "2026-05-23",
    f"{BASE_URL}/blog/isvec-vatandasligi-kac-para-ucretler/": "2026-05-23",
    f"{BASE_URL}/blog/isvec-vatandasi-ile-evlilik/": "2026-05-23",
    f"{BASE_URL}/blog/isvec-vatandasi-turkiyede-kac-gun-kalabilir/": "2026-05-23",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-nedir-2026/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-ne-zaman-agustos-2026/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-basvurusu-ve-kayit/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-konulari-mufredat/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-soru-sayisi-sure-format/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-kimler-muaf-istisnalar/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavina-nasil-hazirlanilir-kaynaklar/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-hakkinda-sikca-sorulanlar/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-pilot-uygulama-utprovningsprov/": "2026-05-22",
    f"{BASE_URL}/blog/isvec-vatandaslik-sinavi-dil-ve-isvecce-seviyesi/": "2026-05-22",
    f"{BASE_URL}/": "2026-05-06",
    f"{BASE_URL}/blog/": "2026-05-06",
    f"{BASE_URL}/blog/isvec-vatandaslik-yeni-kurallar-2026/": "2026-05-06",
    f"{BASE_URL}/blog/isvecte-doktora-arastirmaci-yeni-kurallar-2026/": "2026-05-05",
    f"{BASE_URL}/blog/isvecte-bosanma-tanima-tenfiz-rehberi/": "2026-05-06",
    f"{BASE_URL}/blog/isvecte-bosanan-kadinlar-mal-paylasimi-rehberi/": "2026-05-06",
    f"{BASE_URL}/blog/isvecte-sirket-acmak-rehberi-2026/": "2026-05-04",
    f"{BASE_URL}/blog/isvecte-sommarjobb-vergi-muafiyeti-2026/": "2026-05-21",
    f"{BASE_URL}/blog/isvecte-sommarjobb-bulma-rehberi-2026/": "2026-05-20",
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
