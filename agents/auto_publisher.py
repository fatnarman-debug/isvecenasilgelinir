#!/usr/bin/env python3
import os
import sys
import json
import re
import subprocess
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

# Ensure we can load google-generativeai
try:
    import google.generativeai as genai
except ImportError:
    print("Error: 'google-generativeai' package is not installed. Please install it with 'pip install google-generativeai'.")
    sys.exit(1)

MONTHS_TR = {
    1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan", 5: "Mayıs", 6: "Haziran",
    7: "Temmuz", 8: "Ağustos", 9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık"
}

class AutoPublisher:
    def __init__(self, base_dir="./"):
        self.base_dir = base_dir
        self.config_path = os.path.join(base_dir, "agents/watchdog_config.json")
        self.template_path = os.path.join(base_dir, "agents/blog_template.html")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Configure Gemini API key
        api_key = os.environ.get("GEMINI_API_KEY")
        if not api_key:
            print("\n[WARNING] GEMINI_API_KEY environment variable is not set.")
            print("The script will run in DRY-RUN mode. It will scrape news and print the LLM prompt, but cannot generate posts.")
            print("To run in live mode: GEMINI_API_KEY=your_key python3 agents/auto_publisher.py\n")
            self.dry_run = True
        else:
            genai.configure(api_key=api_key)
            self.dry_run = False
            
    def get_turkish_date(self, dt):
        return f"{dt.day} {MONTHS_TR[dt.month]} {dt.year}"
        
    def check_already_published(self, title):
        # Build a rough slug to check if it exists in blog directory
        slug = re.sub(r'[^a-z0-9\-]', '', title.lower().replace(' ', '-').replace('ı', 'i').replace('ö', 'o').replace('ü', 'u').replace('ç', 'c').replace('ş', 's').replace('ğ', 'g'))
        slug = re.sub(r'-+', '-', slug).strip('-')
        
        blog_dir = os.path.join(self.base_dir, "blog")
        for folder in os.listdir(blog_dir):
            if slug in folder or folder in slug:
                # If there's a folder containing a similar slug name, we assume it's already published
                return True
        return False

    def fetch_article_text(self, url):
        try:
            res = requests.get(url, headers=self.headers, timeout=15)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                # Remove script and style elements
                for script in soup(["script", "style", "nav", "header", "footer"]):
                    script.extract()
                return soup.get_text(separator=' ', strip=True)
        except Exception as e:
            print(f"Error fetching article body: {e}")
        return ""

    def run(self):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Launching AutoPublisher...")
        
        if not os.path.exists(self.config_path):
            print(f"Error: Config not found at {self.config_path}")
            return
            
        with open(self.config_path, 'r') as f:
            config = json.load(f)
            
        today = datetime.now()
        yesterday = today - timedelta(days=1)
        
        today_str = today.strftime("%Y-%m-%d")
        yesterday_str = yesterday.strftime("%Y-%m-%d")
        
        today_tr = self.get_turkish_date(today)
        yesterday_tr = self.get_turkish_date(yesterday)
        
        # We also support Swedish date keywords for today/yesterday (e.g. "idag", "igår" or month names)
        swedish_months = ["januari", "februari", "mars", "april", "maj", "juni", "juli", "augusti", "september", "oktober", "november", "december"]
        
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from sentinel import Sentinel
        sentinel = Sentinel(self.config_path)
        scan_results = sentinel.scan()
        
        new_releases = []
        
        for inst_name, result in scan_results.items():
            if result.get("status") != "Success":
                print(f"Skipping {inst_name} due to status: {result.get('status')}")
                continue
                
            for item in result.get("latest", []):
                title = item.get("title")
                link = item.get("link")
                
                if not title or not link:
                    continue
                    
                # Check if we already published this
                if self.check_already_published(title):
                    print(f"Already published/exists: '{title}'. Skipping.")
                    continue
                    
                print(f"New candidate found: '{title}' ({inst_name})")
                new_releases.append({
                    "title": title,
                    "link": link,
                    "institution": inst_name
                })
                
        if not new_releases:
            print("No new news candidates found that aren't already published.")
            return
            
        print(f"Processing {len(new_releases)} candidates...")
        
        for candidate in new_releases:
            print(f"\n--- Processing: {candidate['title']} ---")
            full_text = self.fetch_article_text(candidate['link'])
            
            prompt = f"""
Bugünün tarihi: {today_str} ({today_tr})
Dünün tarihi: {yesterday_str} ({yesterday_tr})

Sana bir İsveç devlet kurumunun basın açıklaması detaylarını veriyorum:
Başlık: {candidate['title']}
Kaynak Kurum: {candidate['institution']}
Link: {candidate['link']}
Sayfa İçeriği:
{full_text[:8000]}

Soru 1: Bu haber/basın açıklaması {today_str} veya {yesterday_str} tarihinde mi yayınlanmış? 
Metinden veya İsveççe tarih ibarelerinden (örn: "21 maj 2026", "20 maj 2026", "2026-05-21", vb.) bunu analiz et.
Sadece kesinlikle BUGÜN veya DÜN ise devam et. Değilse, JSON çıktısında "is_recent": false olarak belirt ve diğer alanları boş bırak.

Soru 2: Eğer "is_recent" True ise, bu haberi isvecenasilgelinir.com web sitesi için Türkçe bir blog yazısı haline getir. 
Gereksinimler:
- SEO First Page uyumlu, son derece detaylı, bilgilendirici olmalıdır.
- Sitenin hizmetlerini pazarlayan Call to Action (CTA) kısımları barındırmalıdır.
- tasarim.md ve blogyazi.md kurallarına tam uymalıdır.
- Başlıkları H2 ve H3 hiyerarşisinde belirle.
- Varsa verileri ve yasal maddeleri (Örn: Vergi sınırı, form numarası vb.) temiz bir tablo (class="data-table-clean") veya bilgi kutusu (class="elite-info-box") içine yerleştir.
- JSON formatında şu alanları dön:
  1. "is_recent": true/false
  2. "slug": Dosya ve klasör ismi olacak benzersiz slug (örn: "isvecte-sommarjobb-vergi-muafiyeti-2026", sadece küçük harf, rakam ve tire)
  3. "title": Türkçe başlık (örn: "İsveç'te Yaz Çalışanları İçin Vergi Muafiyeti Rehberi 2026")
  4. "meta_description": SEO meta açıklaması (maksimum 160 karakter)
  5. "breadcrumb_name": Breadcrumb'da görünecek kısa isim (örn: "Yaz İşleri Vergi Rehberi")
  6. "category": Yazı kategorisi (örn: "Mali Rehber", "Çalışma İzni & Hukuk")
  7. "lead_paragraph": Yazının en üstünde yer alacak, lead paragraf metni
  8. "body_content": Ana makale gövdesi (H2'ler, H3'ler, paragraflar, listeler, data-table-clean tabloları, elite-info-box kutuları. Görsel ve CTA içermesin, şablondan eklenecektir)
  9. "cta_title": CTA kutusunun başlığı (örn: "İsveç Vergi ve Finans Süreçlerinizde Yanınızdayız")
  10. "cta_text": CTA kutusu metni
  11. "cta_button_text": CTA butonunun üzerindeki yazı
  12. "cover_image_prompt": Görsel oluşturma aracı için Midjourney/DALL-E promptu (İngilizce, yüksek kaliteli, projemizle uyumlu, photorealistic)

Çıktıyı SADECE geçerli bir JSON olarak dön. Markdown kod bloğu ```json ... ``` kullanabilirsin.
"""

            if self.dry_run:
                print("[DRY-RUN] Prompt to Gemini:")
                print(prompt[:1000] + "\n... (truncated) ...")
                continue
                
            try:
                # Use Gemini 1.5 Pro or Flash to generate structured output
                model = genai.GenerativeModel('gemini-1.5-pro')
                response = model.generate_content(prompt)
                
                # Extract JSON block
                response_text = response.text
                json_match = re.search(r'```json\s*(.*?)\s*```', response_text, re.DOTALL)
                if json_match:
                    data = json.loads(json_match.group(1))
                else:
                    data = json.loads(response_text.strip())
                    
                if not data.get("is_recent"):
                    print(f"Skipping candidate '{candidate['title']}' as it was not identified as a today/yesterday release by LLM analysis.")
                    continue
                    
                # We have a valid recent post! Create it
                self.publish_post(data)
                
            except Exception as e:
                print(f"Error calling LLM or parsing output: {e}")
                
    def publish_post(self, data):
        slug = data["slug"]
        title = data["title"]
        meta_description = data["meta_description"]
        breadcrumb_name = data["breadcrumb_name"]
        category = data["category"]
        lead_paragraph = data["lead_paragraph"]
        body_content = data["body_content"]
        cta_title = data["cta_title"]
        cta_text = data["cta_text"]
        cta_button_text = data["cta_button_text"]
        cover_prompt = data["cover_image_prompt"]
        
        today = datetime.now()
        iso_date = today.strftime("%Y-%m-%d")
        date_turkish = self.get_turkish_date(today)
        
        # Schema Markup
        schema_markup = f"""    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "headline": "{title}",
      "image": "https://isvecenasilgelinir.com/assets/images/{slug}.png",
      "datePublished": "{iso_date}T09:00:00+02:00",
      "dateModified": "{iso_date}T12:00:00+02:00",
      "author": {{
        "@type": "Organization",
        "name": "İsveç'e Nasıl Gelinir?"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "İsveç'e Nasıl Gelinir?",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://isvecenasilgelinir.com/assets/images/logo.png"
        }}
      }},
      "description": "{meta_description}"
    }}
    </script>"""

        # Read template
        if not os.path.exists(self.template_path):
            print(f"Error: Template not found at {self.template_path}")
            return
            
        with open(self.template_path, 'r', encoding='utf-8') as f:
            template = f.read()
            
        # Format HTML
        html_output = template.format(
            TITLE=title,
            SLUG=slug,
            META_DESCRIPTION=meta_description,
            SCHEMA_MARKUP=schema_markup,
            BREADCRUMB_NAME=breadcrumb_name,
            CATEGORY=category,
            DATE_TURKISH=date_turkish,
            LEAD_PARAGRAPH=lead_paragraph,
            BODY_CONTENT=body_content,
            CTA_TITLE=cta_title,
            CTA_TEXT=cta_text,
            CTA_BUTTON_TEXT=cta_button_text
        )
        
        # Write post folder and index.html
        post_dir = os.path.join(self.base_dir, "blog", slug)
        os.makedirs(post_dir, exist_ok=True)
        post_file = os.path.join(post_dir, "index.html")
        
        with open(post_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
            
        print(f"\n[SUCCESS] Published new blog post at: {post_file}")
        print(f"Image Cover Prompt: '{cover_prompt}'")
        print(f"Please generate the cover image and save it as: assets/images/{slug}.png")
        
        # Prepend to home index.html
        home_index = os.path.join(self.base_dir, "index.html")
        self.prepend_card(home_index, slug, title, lead_paragraph, category, date_turkish, is_blog_index=False)
        
        # Prepend to blog index.html
        blog_index = os.path.join(self.base_dir, "blog/index.html")
        self.prepend_card(blog_index, slug, title, lead_paragraph, category, date_turkish, is_blog_index=True)
        
        # Update SEO script DATE_MAP
        self.update_seo_script(slug, iso_date)
        
        # Re-run SEO fixes to rebuild sitemap
        print("Rebuilding sitemap and canonical tags...")
        subprocess.run(["python3", "scratch/fix_seo_issues.py"], cwd=self.base_dir)

    def prepend_card(self, file_path, slug, title, lead_paragraph, category, date_turkish, is_blog_index=False):
        if not os.path.exists(file_path):
            print(f"Error: Cannot find list page to update: {file_path}")
            return
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Strip featured-post class and associated styles from existing featured posts
        content = re.sub(r'class="news-card featured-post"', 'class="news-card"', content)
        content = re.sub(r'style="height: 400px; object-fit: cover;"', '', content)

        # 2. Build the new card
        img_path = f"../assets/images/{slug}.png" if is_blog_index else f"assets/images/{slug}.png"
        link_path = f"{slug}/" if is_blog_index else f"blog/{slug}/"
        contact_path = f"../iletisim/" if is_blog_index else f"iletisim/"
        
        category_btn_text = "Uzman Yardımı"
        if "Mali" in category or "Vergi" in category:
            category_btn_text = "Vergi Danışmanlığı"
        elif "Kariyer" in category or "İş" in category:
            category_btn_text = "Kariyer Desteği"
        elif "Hukuk" in category or "Vatandaşlık" in category or "İzin" in category:
            category_btn_text = "Hukuki Danışmanlık"

        card_html = f"""                    <article class="news-card featured-post">
                        <div class="news-img-wrapper">
                            <img src="{img_path}" alt="{title}" class="news-img">
                        </div>
                        <div class="news-content">
                            <span class="news-category">{category}</span>
                            <h3><a href="{link_path}">{title}</a></h3>
                            <p>{lead_paragraph}</p>
                            <a href="{link_path}" class="btn-read-more">Hemen İncele &rarr;</a>
                            <div class="news-meta-footer">
                                <span class="news-date">{date_turkish}</span>
                                <a href="{contact_path}" class="card-contact-link" style="color: #005bb5;">{category_btn_text}</a>
                            </div>
                        </div>
                    </article>"""

        # 3. Inject new card inside <div class="news-grid">
        content = re.sub(r'(<div class="news-grid">)', r'\1\n' + card_html, content, count=1)

        # 4. Limit cards to exactly 5 on homepage (1 featured + 4 normal)
        if not is_blog_index:
            grid_start_tag = '<div class="news-grid">'
            grid_start_idx = content.find(grid_start_tag)
            if grid_start_idx != -1:
                wrapper_tag = '<div class="view-all-wrapper"'
                wrapper_idx = content.find(wrapper_tag, grid_start_idx)
                if wrapper_idx != -1:
                    grid_content_end = content.rfind('</div>', grid_start_idx, wrapper_idx)
                    if grid_content_end != -1:
                        grid_section = content[grid_start_idx + len(grid_start_tag):grid_content_end]
                        articles = re.findall(r'(<article[^>]*>.*?</article>)', grid_section, re.DOTALL)
                        if len(articles) > 5:
                            kept_articles = articles[:5]
                            new_grid_content = "\n" + "\n".join(kept_articles) + "\n                    "
                            content = (
                                content[:grid_start_idx + len(grid_start_tag)] +
                                new_grid_content +
                                content[grid_content_end:]
                            )

        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Prepended card to listing: {file_path}")

    def update_seo_script(self, slug, iso_date):
        script_path = os.path.join(self.base_dir, "scratch/fix_seo_issues.py")
        if not os.path.exists(script_path):
            print(f"Error: SEO script not found at {script_path}")
            return
            
        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        match = re.search(r'(DATE_MAP\s*=\s*\{)', content)
        if match:
            target = match.group(1)
            new_target = target + f'\n    f"{{BASE_URL}}/blog/{slug}/": "{iso_date}",'
            content = content.replace(target, new_target, 1)
            
            with open(script_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated date mapping in SEO script: {script_path}")
        else:
            print("Warning: Could not find DATE_MAP in SEO script to update.")

if __name__ == "__main__":
    publisher = AutoPublisher()
    publisher.run()
