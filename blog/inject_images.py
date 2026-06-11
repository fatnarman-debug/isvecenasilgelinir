import os
import re

folders_and_images = [
    ("yurtdisinda-hastalanmak-ab-saglik-sigortasi-karti", "yurtdisinda-hastalanmak-ab-saglik-sigortasi-karti.png"),
    ("isvecte-turkce-konusan-muhasebeci", "isvecte-turkce-konusan-muhasebeci.png"),
    ("isvecte-gencler-icin-sinirdisi-durdurma-karari-2026", "isvecte-gencler-icin-sinirdisi-durdurma-karari-2026.png"),
    ("isvecte-genc-siginmacilara-oturum-izni-kolayligi-2026", "isvecte-genc-siginmacilara-oturum-izni-kolayligi-2026.png"),
    ("isvecte-evlilik-islemleri-dijital-rehber-2026", "isvecte-evlilik-islemleri-2026.png"),
    ("isvecte-dijital-hindersprovning-yaz-dugunleri", "isvecte-dijital-hindersprovning-yaz-dugunleri.png"),
    ("isvecte-dijital-evlilik-engel-kontrolu-2026", "isvecte-dijital-evlilik-engel-kontrolu-2026.png"),
    ("isvec-pazar-ve-sokak-ticareti-denetimleri-2026", "isvec-pazar-ve-sokak-ticareti-denetimleri-2026.png"),
    ("isvec-guvenlik-tehditleri-icin-yeni-hak-kisitlamalari", "isvec-guvenlik-tehditleri-icin-yeni-hak-kisitlamalari.png"),
    ("isvec-genc-yetiskin-oturma-izni-yeni-duzenleme-2026", "isvec-genc-yetiskin-oturma-izni-yeni-duzenleme-2026.png")
]

base_path = "./"

for f, img_name in folders_and_images:
    idx_path = os.path.join(base_path, f, "index.html")
    if os.path.exists(idx_path):
        with open(idx_path, "r", encoding="utf-8") as file:
            content = file.read()
            
        # find the title to use as alt text
        title_match = re.search(r"<h1[^>]*>(.*?)</h1>", content)
        alt_text = title_match.group(1) if title_match else "İsveç Blog Yazısı"
        
        # Check if already injected (some had logo.png, we should just insert the main image)
        # We want to insert right after the </div> that closes the title div.
        # The title div usually looks like:
        # <div style="margin-top: 40px; margin-bottom: 30px;">
        # ... <h1>...</h1>
        # </div>
        
        # Let's replace the first </h1>\n            </div> with the img tag appended
        img_html = f'\n            <img alt="{alt_text}" src="../../assets/images/{img_name}" style="width: 100%; border-radius: 12px; margin-bottom: 30px; box-shadow: 0 4px 20px rgba(0,0,0,0.08);"/>\n'
        
        # If it's already there (to avoid duplicates):
        if img_name in content:
            # Wait, it might be in the schema.org json-ld block!
            # We want to check if it is in the <article>
            article_match = re.search(r"<article[^>]*>.*?</article>", content, re.DOTALL)
            if article_match and img_name in article_match.group(0):
                print(f"{f}: Already has image inside article.")
                continue
                
        # Inject after </h1></div>
        # Find the position of </h1>
        h1_pos = content.find("</h1>")
        if h1_pos != -1:
            div_close_pos = content.find("</div>", h1_pos)
            if div_close_pos != -1:
                insert_pos = div_close_pos + 6 # length of </div>
                new_content = content[:insert_pos] + img_html + content[insert_pos:]
                
                with open(idx_path, "w", encoding="utf-8") as file:
                    file.write(new_content)
                print(f"{f}: Injected {img_name}")
            else:
                print(f"{f}: Could not find </div> after <h1>")
        else:
            print(f"{f}: Could not find <h1>")
    else:
        print(f"{f}: missing index.html")
