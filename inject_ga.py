import os

ga_snippet = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-P89HGLE2NF"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){dataLayer.push(arguments);}
      gtag('js', new Date());
      gtag('config', 'G-P89HGLE2NF');
    </script>
"""

exclude_dirs = ['skill', 'agents', '.agents', '.git', 'node_modules']

modified_count = 0

for root, dirs, files in os.walk('.'):
    # Skip excluded directories
    dirs[:] = [d for d in dirs if d not in exclude_dirs]
    
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if '</head>' in content and 'G-P89HGLE2NF' not in content:
                # Insert snippet before </head>
                new_content = content.replace('</head>', ga_snippet + '</head>')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                modified_count += 1
                print(f"Injected GA4 into: {filepath}")

print(f"Total files modified: {modified_count}")
