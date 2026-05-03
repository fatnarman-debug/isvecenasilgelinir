import os
import re

def update_favicon(root_dir):
    favicon_link_template = '<link rel="icon" type="image/png" href="{path}favicon.png">'
    
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                
                # Calculate relative path to root
                rel_path = os.path.relpath(root_dir, root)
                if rel_path == ".":
                    rel_to_root = ""
                else:
                    rel_to_root = rel_path + "/"
                
                favicon_link = favicon_link_template.format(path=rel_to_root)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Check if favicon already exists
                if 'rel="icon"' in content or 'rel="shortcut icon"' in content:
                    continue
                
                # Insert after <head> or <meta charset>
                if '<head>' in content:
                    new_content = content.replace('<head>', f'<head>\n    {favicon_link}')
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated: {file_path}")

if __name__ == "__main__":
    update_favicon("/Users/fatnar/Documents/isvecenasilgelinir")
