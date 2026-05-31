#!/usr/bin/env python3
import os
import sys
import json
import re
import asyncio
import urllib.parse
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
import pydantic

# Load environment variables from .env file if present
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Ensure we can load google-antigravity and google-genai
try:
    from google.antigravity import Agent, LocalAgentConfig
    from google.antigravity.types import CustomSystemInstructions
    from google import genai
except ImportError as e:
    print(f"Error importing SDK: {e}. Please ensure google-antigravity and google-genai are installed.")
    sys.exit(1)

MONTHS_TR = {
    1: "Ocak", 2: "Şubat", 3: "Mart", 4: "Nisan", 5: "Mayıs", 6: "Haziran",
    7: "Temmuz", 8: "Ağustos", 9: "Eylül", 10: "Ekim", 11: "Kasım", 12: "Aralık"
}

# Define the target schema for the Writer Agent using Pydantic
class BlogPostDraft(pydantic.BaseModel):
    is_recent: bool
    slug: str
    title: str
    meta_description: str
    breadcrumb_name: str
    category: str
    lead_paragraph: str
    body_content: str  # HTML containing headings H2/H3, tables, info boxes. Excludes cover image and CTA box.
    cta_title: str
    cta_text: str
    cta_button_text: str
    cover_image_prompt: str  # Detailed prompt in English for Imagen 3.0

# Define the target schema for the Editor Agent using Pydantic
class EditorialReview(pydantic.BaseModel):
    approved: bool
    feedback: str

# Custom Tools for Competitor Analysis
def search_competitors(query: str) -> str:
    """
    Search Google to find top pages about a topic in order to check what competitors have written.
    
    Args:
        query: Search query, e.g. "İsveç sommarjobb vergi muafiyeti 2026"
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            results = []
            for a in soup.select('.result__snippet')[:5]:
                results.append(a.get_text(strip=True))
            if results:
                return "\n".join(results)
    except Exception as e:
        return f"Search failed: {e}"
    return "No competitor content found."

def fetch_url(url: str) -> str:
    """
    Fetch the content of a competitor's webpage to analyze their content scope and details.
    
    Args:
        url: URL of the webpage to scrape
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    try:
        res = requests.get(url, headers=headers, timeout=10)
        if res.status_code == 200:
            soup = BeautifulSoup(res.text, 'html.parser')
            for tag in soup(["script", "style", "nav", "header", "footer"]):
                tag.extract()
            return soup.get_text(separator=' ', strip=True)[:4000]
    except Exception as e:
        return f"Fetch failed: {e}"
    return "No content."


class SEOContentEngine:
    def __init__(self, base_dir="./"):
        self.base_dir = os.path.abspath(base_dir)
        self.config_path = os.path.join(self.base_dir, "agents/watchdog_config.json")
        self.template_path = os.path.join(self.base_dir, "agents/blog_template.html")
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        }
        
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            print("\n[WARNING] GEMINI_API_KEY environment variable is not set.")
            print("The system will run in DRY-RUN mode. It will scrape news but cannot call LLMs or generate posts.\n")
            self.dry_run = True
            self.genai_client = None
        else:
            self.dry_run = False
            self.genai_client = genai.Client(api_key=self.api_key)

    def get_turkish_date(self, dt):
        return f"{dt.day} {MONTHS_TR[dt.month]} {dt.year}"

    def check_already_published(self, title):
        slug = re.sub(r'[^a-z0-9\-]', '', title.lower().replace(' ', '-').replace('ı', 'i').replace('ö', 'o').replace('ü', 'u').replace('ç', 'c').replace('ş', 's').replace('ğ', 'g'))
        slug = re.sub(r'-+', '-', slug).strip('-')
        
        blog_dir = os.path.join(self.base_dir, "blog")
        if not os.path.exists(blog_dir):
            return False
            
        for folder in os.listdir(blog_dir):
            if slug in folder or folder in slug:
                return True
        return False

    def fetch_article_text(self, url):
        if url == "https://www.migrationsverket.se/test-medborgarskapsprov":
            return """
            Migrationsverket, 1 Haziran 2026 tarihli açıklamasında İsveç vatandaşlığı için dil ve toplumsal bilgi sınavı (samhällskunskapsprov / medborgarskapsprov) pilot uygulamasının genişletileceğini duyurdu. 
            Yeni düzenlemeyle birlikte pilot bölgelere Göteborg ve Malmö de ekleniyor. Sınavda adayların en az B1 seviyesinde İsveççe dil bilgisine ve İsveç'in anayasal düzeni ile temel toplumsal yapısına hakim olmaları bekleniyor.
            Sınava başvurular ve kayıt işlemleri 1 Temmuz 2026 itibarıyla online sistem üzerinden başlayacaktır. Ücretler ve muafiyet şartları daha önce duyurulan rehberle aynı kalmıştır.
            """
        try:
            res = requests.get(url, headers=self.headers, timeout=15)
            if res.status_code == 200:
                soup = BeautifulSoup(res.text, 'html.parser')
                for script in soup(["script", "style", "nav", "header", "footer"]):
                    script.extract()
                return soup.get_text(separator=' ', strip=True)
        except Exception as e:
            print(f"Error fetching article body: {e}")
        return ""

    async def run(self):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Launching SEO Content Engine...")
        
        candidates = []
        
        # Test mode override
        if len(sys.argv) > 1 and sys.argv[1] == "--test":
            print("[TEST MODE] Running with a mock candidate...")
            candidates.append({
                "title": "İsveç Vatandaşlık Sınavı Uygulaması Genişletiliyor",
                "link": "https://www.migrationsverket.se/test-medborgarskapsprov",
                "institution": "Migrationsverket"
            })
        else:
            if not os.path.exists(self.config_path):
                print(f"Error: Config not found at {self.config_path}")
                return
                
            with open(self.config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
                
            # Initialize Sentinel to scan sites
            sys.path.append(os.path.join(self.base_dir, "agents"))
            from sentinel import Sentinel
            sentinel = Sentinel(self.config_path)
            scan_results = sentinel.scan()
            
            for inst_name, result in scan_results.items():
                if result.get("status") != "Success":
                    print(f"Skipping {inst_name} due to status: {result.get('status')}")
                    continue
                    
                for item in result.get("latest", []):
                    title = item.get("title")
                    link = item.get("link")
                    
                    if not title or not link:
                        continue
                        
                    if self.check_already_published(title):
                        print(f"Already published/exists: '{title}'. Skipping.")
                        continue
                        
                    print(f"New candidate found: '{title}' ({inst_name})")
                    candidates.append({
                        "title": title,
                        "link": link,
                        "institution": inst_name
                    })
                    
        if not candidates:
            print("No new news candidates found that aren't already published.")
            return
            
        if self.dry_run:
            print("[DRY-RUN] Found candidates, but skipping LLM execution as GEMINI_API_KEY is not set.")
            return

        for candidate in candidates:
            await self.process_candidate(candidate)

    async def process_candidate(self, candidate):
        print(f"\n==========================================")
        print(f"Processing candidate: {candidate['title']}")
        print(f"==========================================")
        
        full_text = self.fetch_article_text(candidate['link'])
        if not full_text:
            print("Could not fetch page body. Skipping.")
            return

        today = datetime.now()
        today_str = today.strftime("%Y-%m-%d")
        last_week = today - timedelta(days=7)
        last_week_str = last_week.strftime("%Y-%m-%d")

        # Configure the Writer Agent
        writer_instructions = f"""
        Sen isvecenasilgelinir.com sitesi için uzman bir Türkçe SEO yazarı ve İsveç göçmenlik danışmanısın.
        Görevin, sana verilen İsveççe resmi duyuruyu incelemek, eğer son 1 hafta içinde yayınlanmış güncel bir haber ise onu son derece kapsamlı ve bilgilendirici bir Türkçe blog rehberine dönüştürmektir.

        Bugünün Tarihi: {today_str}
        Son 1 Haftanın Başlangıç Tarihi: {last_week_str}

        Kurallar:
        1. İsveççe metindeki tarih bilgilerini analiz et. Eğer son 1 hafta içinde yayınlanmış (yani {last_week_str} ile {today_str} arasında) GÜNCEL bir haber ise "is_recent": true yap ve rehber yazmaya başla. Değilse "is_recent": false yap ve diğer tüm alanları boş bırak.
        2. Yazacağın Türkçe blog yazısı, internetteki diğer rakip yazılardan çok daha kapsamlı ve güncel olmalıdır. Bunun için gerekirse `search_competitors` ve `fetch_url` araçlarını kullanarak competitor analizi yap.
        3. SEO Optimizasyonu:
           - Başlıkları H2 ve H3 hiyerarşisi ile kurgula. H1 kullanma (şablonda otomatik basılacaktır).
           - Yasal sayısal verileri, kuralları ve limitleri temiz bir tablo (`class="data-table-clean"`) veya zengin bilgi kutusu (`class="elite-info-box"`) içine yerleştir.
           - `https://sverigemedborgarskapsprov.com` sitesine DOFOLLOW backlinkler ver.
             - Bu linklerden biri yazının başındaki paragraflarda, diğeri ise ortasındaki uygun bir paragrafın veya kutunun içinde olmalıdır.
             - Çapa metinleri (anchor text) olarak şunlardan en uygun olanlarını seç: "İsveç Vatandaşlık Testi", "İsveç Vatandaşlık Sınavı", "sverigemedborgarskapsprov.com".
             - Örnek: `<a href="https://sverigemedborgarskapsprov.com" rel="dofollow">İsveç Vatandaşlık Sınavı</a>`
             - En altta ise referanslar kısmında dofollow link işareti ekle.
        4. Arayüz & Tasarım Kuralları:
           - Metin içinde gereksiz çizgilerden kaçın, sade, premium ve modern bir dil kullan.
        5. Kapak görseli oluşturmak için detaylı İngilizce bir Imagen 3.0 promptu üret (`cover_image_prompt`). Örnek: "Minimalist modern 3D vector style concept of Swedish student permit, blue and yellow color tones, soft shadows, 16:9 aspect ratio, high resolution".
        """

        writer_config = LocalAgentConfig(
            model="gemini-3.5-flash",
            system_instructions=CustomSystemInstructions(text=writer_instructions),
            tools=[search_competitors, fetch_url],
            response_schema=BlogPostDraft
        )

        # Configure the Editor Agent
        editor_instructions = """
        Sen isvecenasilgelinir.com blogunun baş editörüsün. Görevin, yazar ajanın hazırladığı Türkçe blog yazısı taslağını sıkı bir denetimden geçirmektir.
        
        Aşağıdaki kriterleri kontrol et:
        1. Backlink Kontrolü: 
           - Yazının başında ve ortasında `https://sverigemedborgarskapsprov.com` adresine giden DOFOLLOW linkleri bulunuyor mu?
           - Bu linklerin `rel="dofollow"` parametresi var mı?
           - Çapa metinleri (Anchor Text) "İsveç Vatandaşlık Testi", "İsveç Vatandaşlık Sınavı" veya "sverigemedborgarskapsprov.com" olarak doğru kullanılmış mı?
           - Yazının en altında referanslar kısmında link bulunuyor mu?
        2. Tasarım & Hiyerarşi Kontrolü:
           - Başlıklar H2 ve H3 şeklinde mi düzenlenmiş? H1 başlığı taslak içinde OLMAMALIDIR (şablon otomatik olarak basıyor).
           - Tablolar `class="data-table-clean"`, bilgi kutuları `class="elite-info-box"` sınıflarını kullanıyor mu?
           - Kod yapısında veya metinde biçimlendirme hataları var mı?
        3. SEO & Dil Kalitesi:
           - Türkçe dil bilgisi, tonlama premium mu?
           - Meta açıklaması 160 karakterden kısa ve çekici mi?

        Eğer tüm kriterler eksiksiz sağlanıyorsa, `approved: true` ve `feedback: ""` dön.
        Eksikler varsa, `approved: false` yap ve yazarın düzeltebilmesi için son derece net, düzeltici bir `feedback` yaz.
        """

        editor_config = LocalAgentConfig(
            model="gemini-3.5-flash",
            system_instructions=CustomSystemInstructions(text=editor_instructions),
            response_schema=EditorialReview
        )

        draft = None
        loop_count = 0
        max_loops = 3
        feedback_msg = "Lütfen İsveççe duyurudan yeni bir Türkçe blog yazısı taslağı oluştur."

        async with Agent(writer_config) as writer:
            async with Agent(editor_config) as editor:
                while loop_count < max_loops:
                    loop_count += 1
                    print(f"Turn {loop_count}: Writer is generating/updating draft...")
                    
                    writer_prompt = f"""
                    Aşağıdaki İsveççe duyuruyu incele ve kurallara uygun şekilde Türkçe blog taslağını oluştur.
                    
                    Duyuru Kurumu: {candidate['institution']}
                    Duyuru Linki: {candidate['link']}
                    Başlık: {candidate['title']}
                    
                    Duyuru İçeriği:
                    {full_text[:8000]}
                    
                    Editörden gelen geri bildirim:
                    {feedback_msg}
                    """
                    
                    writer_resp = await writer.chat(writer_prompt)
                    draft = await writer_resp.structured_output()
                    
                    if not draft:
                        print("Failed to get structured draft from Writer.")
                        return
                        
                    if not draft.get("is_recent"):
                        print(f"Skipping: Writer identified this article as not recent enough (older than 1 week).")
                        return
                        
                    print("Draft generated successfully. Sending to Editor for review...")
                    
                    editor_prompt = f"""
                    Lütfen aşağıdaki taslağı kurallara göre incele:
                    
                    Başlık: {draft['title']}
                    Kategori: {draft['category']}
                    Meta Açıklama: {draft['meta_description']}
                    Lead Paragrafı: {draft['lead_paragraph']}
                    Gövde İçeriği:
                    {draft['body_content']}
                    
                    Referans Linkler / CTA Bilgileri:
                    CTA Başlık: {draft['cta_title']}
                    CTA Metin: {draft['cta_text']}
                    """
                    
                    editor_resp = await editor.chat(editor_prompt)
                    review = await editor_resp.structured_output()
                    
                    if not review:
                        print("Failed to get structured review from Editor. Approving by default.")
                        break
                        
                    if review.get("approved"):
                        print("Editorial Review passed successfully! Publishing post...")
                        break
                    else:
                        print(f"Editorial Review rejected. Feedback: {review.get('feedback')}")
                        feedback_msg = f"Editör Reddi Bildirimi: {review.get('feedback')}"
                
                # If we broke out of loop or completed loops, publish if we have a draft
                if draft and (loop_count == max_loops or review.get("approved", True)):
                    await self.publish_post(draft)
                else:
                    print("Could not get an approved draft after maximum iteration loops.")

    async def publish_post(self, draft):
        slug = draft["slug"]
        title = draft["title"]
        meta_description = draft["meta_description"]
        breadcrumb_name = draft["breadcrumb_name"]
        category = draft["category"]
        lead_paragraph = draft["lead_paragraph"]
        body_content = draft["body_content"]
        cta_title = draft["cta_title"]
        cta_text = draft["cta_text"]
        cta_button_text = draft["cta_button_text"]
        cover_prompt = draft["cover_image_prompt"]
        
        today = datetime.now()
        iso_date = today.strftime("%Y-%m-%d")
        date_turkish = self.get_turkish_date(today)
        
        # 1. Automate Cover Image generation via Imagen 3.0
        image_relative_path = f"assets/images/{slug}.png"
        image_absolute_path = os.path.join(self.base_dir, image_relative_path)
        
        print(f"Generating cover image with Imagen 3.0 for prompt: '{cover_prompt}'...")
        try:
            image_result = self.genai_client.models.generate_images(
                model='imagen-3.0-generate-002',
                prompt=cover_prompt,
                config=dict(
                    number_of_images=1,
                    output_mime_type="image/png",
                    aspect_ratio="16:9"
                )
            )
            if image_result.generated_images:
                image_bytes = image_result.generated_images[0].image.image_bytes
                os.makedirs(os.path.dirname(image_absolute_path), exist_ok=True)
                with open(image_absolute_path, 'wb') as img_f:
                    img_f.write(image_bytes)
                print(f"[SUCCESS] Cover image saved to: {image_absolute_path}")
            else:
                print("[WARNING] Imagen did not return any image. Using a fallback color placeholder.")
                self.write_fallback_image(image_absolute_path)
        except Exception as e:
            print(f"[WARNING] Error generating image via SDK: {e}. Writing fallback placeholder.")
            self.write_fallback_image(image_absolute_path)

        # 2. Prepare schema and HTML
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

        if not os.path.exists(self.template_path):
            print(f"Error: Template not found at {self.template_path}")
            return
            
        with open(self.template_path, 'r', encoding='utf-8') as f:
            template = f.read()
            
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
        
        post_dir = os.path.join(self.base_dir, "blog", slug)
        os.makedirs(post_dir, exist_ok=True)
        post_file = os.path.join(post_dir, "index.html")
        
        with open(post_file, 'w', encoding='utf-8') as f:
            f.write(html_output)
            
        print(f"[SUCCESS] Published new blog post at: {post_file}")
        
        # Prepend to homepage index.html
        home_index = os.path.join(self.base_dir, "index.html")
        self.prepend_card(home_index, slug, title, lead_paragraph, category, date_turkish, is_blog_index=False)
        
        # Prepend to blog index.html
        blog_index = os.path.join(self.base_dir, "blog/index.html")
        self.prepend_card(blog_index, slug, title, lead_paragraph, category, date_turkish, is_blog_index=True)
        
        # Update canonical SEO list map in fix_seo_issues.py
        self.update_seo_script(slug, iso_date)
        
        # Re-run SEO scripts to rebuild sitemap and fix missing canonicals
        print("Rebuilding sitemap and canonical tags...")
        import subprocess
        subprocess.run(["python3", "scratch/fix_seo_issues.py"], cwd=self.base_dir)

    def write_fallback_image(self, path):
        # Create a tiny 1x1 pixel PNG or write empty bytes so it exists
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # 1x1 transparent PNG bytes
        fallback_png = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01\x08\x06\x00\x00\x00\x1f\x15c4\x00\x00\x00\rIDATx\x9cc\xfc\xcf\xe0\x00\x03\x00\x01\xbd\x00\x18\xda\x18g\x83\x00\x00\x00\x00IEND\xaeB`\x82'
        with open(path, 'wb') as f:
            f.write(fallback_png)

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
    engine = SEOContentEngine()
    asyncio.run(engine.run())
