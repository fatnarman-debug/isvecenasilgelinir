import os
import re

header_template = """    <header class="site-header">
        <div class="container">
            <a href="../../" class="logo">
                <img src="../../assets/images/logo.png" alt="İsveç'e Nasıl Gelinir?" class="logo-img">
            </a>
            <nav class="main-nav">
                <ul>
                    <li><a href="../../">Ana Sayfa</a></li>
                    <li><a href="../../blog/" class="active">Blog & Rehberler</a></li>
                    <li><a href="../../hakkimizda/">Hakkımızda</a></li>
                    <li><a href="../../iletisim/">İletişim</a></li>
                    <li class="mobile-only"><a href="../../hukuki-yardim/">Hukuki Yardım</a></li>
                </ul>
            </nav>
            <a href="../../hukuki-yardim/" class="header-legal-btn">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h18"/></svg>
                Hukuki Yardım
            </a>
            <button class="menu-toggle" aria-label="Menüyü Aç">
                <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="3" y1="12" x2="21" y2="12"></line><line x1="3" y1="6" x2="21" y2="6"></line><line x1="3" y1="18" x2="21" y2="18"></line></svg>
            </button>
        </div>
    </header>"""

blog_dir = 'blog'
for root, dirs, files in os.walk(blog_dir):
    # Skip the root blog directory (handled manually or separately)
    if root == blog_dir:
        continue
    for file in files:
        if file == 'index.html':
            path = os.path.join(root, file)
            print(f"Fixing header in: {path}")
            with open(path, 'r') as f:
                content = f.read()
            
            # Find the header block and replace it
            new_content = re.sub(r'<header class="site-header">.*?</header>', header_template, content, flags=re.DOTALL)
            
            with open(path, 'w') as f:
                f.write(new_content)
