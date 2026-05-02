import os
import glob

def inject_marketing_assets():
    html_files = glob.glob("**/*.html", recursive=True)
    
    for file_path in html_files:
        if file_path in ['index.html', 'quiz/index.html']:
            continue
            
        # Skip assets or other non-content dirs if any
        if 'assets/' in file_path or 'scratch/' in file_path:
            continue
            
        print(f"Processing {file_path}...")
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Determine depth
        depth = file_path.count('/')
        prefix = "../" * depth
        
        current_css = f'    <link rel="stylesheet" href="{prefix}assets/css/marketing.css">'
        current_js = f'    <script src="{prefix}assets/js/marketing.js"></script>'
        
        # Remove existing (possibly wrong) marketing links first to avoid duplicates
        import re
        content = re.sub(r'    <link rel="stylesheet" href=".*?assets/css/marketing.css">', '', content)
        content = re.sub(r'    <script src=".*?assets/js/marketing.js"></script>', '', content)
        
        # Inject CSS before </head>
        content = content.replace('</head>', f'{current_css}\n</head>')
            
        # Inject JS before </body>
        content = content.replace('</body>', f'{current_js}\n</body>')
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

if __name__ == "__main__":
    inject_marketing_assets()
