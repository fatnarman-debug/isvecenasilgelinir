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
        # This is a simplified version of the site's layout
        # In practice, it should match the premium design rules in tasarim.md
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
    <main class="container" style="margin-top: 40px; max-width: 800px;">
        <article class="post-detail">
            <span class="news-category">{category}</span>
            <h1>{title}</h1>
            <p class="post-meta">{date}</p>
            <img src="../../{image_path}" alt="{title}" style="width: 100%; border-radius: 12px; margin: 20px 0;">
            <div class="post-content">
                {content}
            </div>
            <div class="cta-box" style="background: #f8fafc; padding: 30px; border-radius: 12px; margin-top: 40px; border: 1px solid #e2e8f0;">
                <h3>Hukuki Yardıma mı İhtiyacınız Var?</h3>
                <p>İsveç'te Türkçe konuşan uzman avukatlarımızla oturum ve çalışma izni süreçlerinizi güvenle yönetin.</p>
                <a href="../../iletisim/" class="btn btn-primary">Bize Ulaşın</a>
            </div>
        </article>
    </main>
    <footer class="site-footer" style="margin-top: 80px;">
        <div class="container" style="text-align: center;">
            <p>&copy; 2026 İsveç'e Nasıl Gelinir?</p>
        </div>
    </footer>
</body>
</html>"""
        return template

    def _update_listings(self, slug, title, image_path, category, date):
        # Update blog/index.html and root index.html
        # Logic to find news-grid and prepend the new article
        # This is a simplified regex-based approach
        for file_to_update in ["index.html", "blog/index.html"]:
            path = os.path.join(self.base_dir, file_to_update)
            if not os.path.exists(path): continue
            
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Create the card HTML
            prefix = "../" if "blog/" in file_to_update else ""
            card_html = f"""
                    <article class="news-card">
                        <div class="news-img-wrapper">
                            <span class="card-badge info">{category.split(' & ')[0]}</span>
                            <img src="{prefix}{image_path}" alt="{title}" class="news-img">
                        </div>
                        <div class="news-content">
                            <span class="news-category">{category}</span>
                            <h3><a href="{prefix}blog/{slug}/">{title}</a></h3>
                            <p>{title} hakkında detaylı rehber ve güncel bilgiler.</p>
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
