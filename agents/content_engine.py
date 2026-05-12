import os
import sys
import json
from datetime import datetime
import re

class ContentEngine:
    def __init__(self, base_dir):
        self.base_dir = base_dir
        self.blog_dir = os.path.join(base_dir, "blog")
        self.assets_dir = os.path.join(base_dir, "assets/images")
        
    def create_blog_post(self, slug, title, content, image_path, category, date=None):
        if not date:
            date = datetime.now().strftime("%d %B %Y")
            
        post_dir = os.path.join(self.blog_dir, slug)
        os.makedirs(post_dir, exist_ok=True)
        
        # Simple HTML Template integration
        # (In a real scenario, this would load a more complex template.html)
        html_content = self._generate_html(title, content, image_path, category, date)
        
        file_path = os.path.join(post_dir, "index.html")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"Blog post created: {file_path}")
        self._update_listings(slug, title, image_path, category, date)
        
    def _generate_html(self, title, content, image_path, category, date):
        template = f"""<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | İsveç'e Nasıl Gelinir?</title>
    <link rel="stylesheet" href="../../assets/css/index.css">
    <link rel="stylesheet" href="../../assets/css/components.css">
    <link rel="stylesheet" href="../../assets/css/marketing.css">
</head>
<body>
    <header class="site-header">
        <div class="container">
            <a href="../../" class="logo"><img src="../../assets/images/logo.png" alt="Logo" class="logo-img"></a>
            <nav class="main-nav">
                <ul>
                    <li><a href="../../">Ana Sayfa</a></li>
                    <li><a href="../" class="active">Blog</a></li>
                    <li><a href="../../iletisim/">İletişim</a></li>
                </ul>
            </nav>
        </div>
    </header>
    <main class="container" style="margin-top: 40px; max-width: 900px;">
        <article class="post-detail">
            <header class="post-header" style="text-align: center; margin-bottom: 40px;">
                <span class="card-badge info" style="position: static; display: inline-block;">{category.split(' & ')[0]}</span>
                <h1 style="margin-top: 20px;">{title}</h1>
                <p class="post-meta">{date}</p>
            </header>
            <img src="../../{image_path}" alt="{title}" style="width: 100%; border-radius: 16px; margin-bottom: 40px;">
            <div class="post-content">
                {content}
            </div>
            <div class="cta-box">
                <h2>Sürecinizi Uzmanlara Emanet Edin</h2>
                <p>İsveç göç yasaları karmaşıktır. Hata payınızı sıfıra indirmek ve en hızlı sonucu almak için Türkçe konuşan avukat ekibimizle iletişime geçin.</p>
                <div class="btn-group">
                    <a href="../../iletisim/" class="btn btn-primary">Ücretsiz Ön Değerlendirme</a>
                    <a href="https://wa.me/4600000000" class="btn btn-whatsapp">WhatsApp'tan Yazın</a>
                </div>
            </div>
        </article>
    </main>
    <footer class="site-footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-col">
                    <img src="../../assets/images/logo.png" alt="İsveç'e Nasıl Gelinir Logo" class="footer-logo">
                    <p>İsveç hayalinizi gerçeğe dönüştürmek için ihtiyacınız olan tüm rehberlik, danışmanlık ve güncel bilgiler tek bir platformda.</p>
                </div>
                <div class="footer-col">
                    <h3>Hızlı Linkler</h3>
                    <ul>
                        <li><a href="../../">Ana Sayfa</a></li>
                        <li><a href="../">Blog & Rehberler</a></li>
                        <li><a href="../../quiz/">İsveç Hazırlık Testi</a></li>
                        <li><a href="../../hakkimizda/">Hakkımızda</a></li>
                        <li><a href="../../iletisim/">İletişim</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>Hizmetlerimiz</h3>
                    <ul>
                        <li><a href="../../#">Oturum İzni</a></li>
                        <li><a href="../../#">İş Bulma Danışmanlığı</a></li>
                        <li><a href="../../#">Eğitim ve Üniversite</a></li>
                        <li><a href="../../#">Şirket Kurulumu</a></li>
                    </ul>
                </div>
                <div class="footer-col">
                    <h3>İletişim</h3>
                    <p><strong>Email:</strong> info@isvecenasilgelinir.com</p>
                    <p><strong>Adres:</strong> Stockholm, İsveç</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 İsveç'e Nasıl Gelinir? Tüm hakları saklıdır.</p>
            </div>
        </div>
    </footer>
    <nav class="bottom-nav">
        <a href="../../" class="nav-item">Ana Sayfa</a>
        <a href="../" class="nav-item active">Rehberler</a>
        <a href="../../iletisim/" class="nav-item">İletişim</a>
    </nav>
</body>
</html>"""
        return template

    def _update_listings(self, slug, title, image_path, category, date):
        # Update blog/index.html and root index.html
        for file_to_update in ["index.html", "blog/index.html"]:
            path = os.path.join(self.base_dir, file_to_update)
            if not os.path.exists(path): continue
            
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # 1. Strip existing featured-post class and associated inline styles
            content = content.replace('news-card featured-post', 'news-card')
            content = content.replace('style="height: 400px; object-fit: cover;"', '')
            
            # 2. Create the NEW card HTML as featured-post
            prefix = "../" if "blog/" in file_to_update else ""
            card_html = f"""
                <article class="news-card featured-post">
                    <div class="news-img-wrapper">
                        <span class="card-badge info" style="position: absolute; top: 20px; left: 20px; z-index: 10;">Yeni Rehber</span>
                        <img src="{prefix}{image_path}" alt="{title}" class="news-img" style="height: 400px; object-fit: cover;">
                    </div>
                    <div class="news-content">
                        <span class="news-category">{category}</span>
                        <h3><a href="{prefix}blog/{slug}/">{title}</a></h3>
                        <p>{title} hakkında kapsamlı ve en güncel bilgileri içeren uzman rehberimiz yayınlandı.</p>
                        <a href="{prefix}blog/{slug}/" class="btn-read-more">Hemen Oku &rarr;</a>
                        <div class="news-meta-footer">
                            <span class="news-date">{date}</span>
                            <a href="{prefix}iletisim/" class="card-contact-link">Uzman Yardımı</a>
                        </div>
                    </div>
                </article>"""
            
            # Inject after <div class="news-grid">
            new_content = re.sub(r'(<div class="news-grid">)', r'\1' + card_html, content, count=1)
            
            with open(path, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"Updated listing: {path}")

if __name__ == "__main__":
    # Example usage: python agents/content_engine.py slug title "content" image_path category
    if len(sys.argv) > 1:
        engine = ContentEngine("./")
        # In a real tool, we'd use argparse
        pass
