import os
import bs4

def get_first_paragraph(soup):
    for p in soup.find_all('p'):
        text = p.get_text(strip=True)
        if len(text) > 20:
            return text[:155] + '...' if len(text) > 155 else text
    return "İsveç'e yerleşmek, iş bulmak, şirket kurmak ve vatandaşlık almak isteyenler için kapsamlı rehber ve danışmanlık hizmetleri."

def process_html_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    soup = bs4.BeautifulSoup(html_content, 'html.parser')
    head = soup.find('head')
    if not head:
        return False
        
    modified = False
    
    # 1. Title
    title_tag = soup.find('title')
    title_text = title_tag.get_text(strip=True) if title_tag else "İsveç'e Nasıl Gelinir - Rehber ve Danışmanlık"
    
    # 2. Meta description
    desc_tag = soup.find('meta', attrs={'name': 'description'})
    desc_text = ""
    if desc_tag and desc_tag.get('content'):
        desc_text = desc_tag['content'].strip()
    else:
        desc_text = get_first_paragraph(soup)
        new_desc = soup.new_tag('meta', attrs={'name': 'description', 'content': desc_text})
        head.append(new_desc)
        head.append('\n    ')
        modified = True

    # 3. Open Graph Tags
    og_tags = {
        'og:title': title_text,
        'og:description': desc_text,
        'og:type': 'website',
        'og:url': 'https://isvecenasilgelinir.com/',
        'og:image': 'https://isvecenasilgelinir.com/favicon.png'
    }
    
    for prop, content in og_tags.items():
        existing_og = soup.find('meta', attrs={'property': prop})
        if not existing_og:
            new_og = soup.new_tag('meta', attrs={'property': prop, 'content': content})
            head.append(new_og)
            head.append('\n    ')
            modified = True
            
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
        print(f"Updated: {filepath}")
        return True
    return False

def main():
    root_dir = "."
    exclude_dirs = {'.agents', '.git', 'scratch', 'skill'}
    
    count = 0
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Exclude directories
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        
        for filename in filenames:
            if filename.endswith(".html"):
                filepath = os.path.join(dirpath, filename)
                if process_html_file(filepath):
                    count += 1
                    
    print(f"Total files updated: {count}")

if __name__ == "__main__":
    main()
