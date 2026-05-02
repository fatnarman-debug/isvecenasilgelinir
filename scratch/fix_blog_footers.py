import os
import re

footer_html = """    <footer class="site-footer">
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
                        <li><a href="../../blog/">Blog & Rehberler</a></li>
                        <li><a href="../../hakkimizda/">Hakkımızda</a></li>
                        <li><a href="../../iletisim/">İletişim</a></li>
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

    <!-- Mobile Bottom Navigation -->
    <nav class="bottom-nav" style="display: none;">
        <a href="../../" class="nav-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"></path><polyline points="9 22 9 12 15 12 15 22"></polyline></svg>
            Ana Sayfa
        </a>
        <a href="../../blog/" class="nav-item active">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5v-15A2.5 2.5 0 0 1 6.5 2H20v20H6.5a2.5 2.5 0 0 1 0-5H20"></path></svg>
            Rehberler
        </a>
        <a href="../../hukuki-yardim/" class="nav-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h18"/></svg>
            Hukuki
        </a>
        <a href="../../iletisim/" class="nav-item">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"></path></svg>
            İletişim
        </a>
    </nav>"""

blog_dir = 'blog'
for root, dirs, files in os.walk(blog_dir):
    for file in files:
        if file == 'index.html':
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace footer and add mobile nav
            new_content = re.sub(r'<footer.*?</footer>', footer_html, content, flags=re.DOTALL)
            
            # Check if bottom-nav was already there, if not, it was added by footer_html replacement anyway 
            # (assuming it was right before or after footer)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated: {filepath}")
