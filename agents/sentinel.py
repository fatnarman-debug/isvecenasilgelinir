import json
import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Sentinel:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
    def scan(self):
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting scan for {self.config['system_name']}...")
        all_results = {}
        
        for inst in self.config['institutions']:
            print(f"Checking {inst['name']}...")
            try:
                response = requests.get(inst['url'], headers=self.headers, timeout=15)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.text, 'html.parser')
                    items = []
                    
                    # Generic selector extraction based on config
                    # Defaulting to some common patterns if selectors aren't perfect
                    news_selector = inst.get('selectors', {}).get('news_item', 'h3')
                    date_selector = inst.get('selectors', {}).get('date', 'span')
                    
                    found_elements = soup.select(news_selector)[:5] # Get last 5
                    for el in found_elements:
                        title = el.get_text(strip=True)
                        link = ""
                        if el.name == 'a':
                            link = el.get('href', '')
                        elif el.find('a'):
                            link = el.find('a').get('href', '')
                        
                        # Fix relative links
                        if link and not link.startswith('http'):
                            base_url = inst['url'].split('/')[0] + "//" + inst['url'].split('/')[2]
                            link = base_url + link
                            
                        items.append({
                            "title": title,
                            "link": link,
                            "institution": inst['name']
                        })
                    
                    all_results[inst['name']] = {
                        "status": "Success",
                        "items_found": len(items),
                        "latest": items[:2]
                    }
                else:
                    all_results[inst['name']] = {"status": f"Error: HTTP {response.status_code}"}
            except Exception as e:
                all_results[inst['name']] = {"status": f"Error: {str(e)}"}
                
        return all_results

if __name__ == "__main__":
    # Ensure we are in the right directory
    config_path = "agents/watchdog_config.json"
    if os.path.exists(config_path):
        sentinel = Sentinel(config_path)
        scan_results = sentinel.scan()
        print("\n--- SCAN SUMMARY ---")
        print(json.dumps(scan_results, indent=2, ensure_ascii=False))
    else:
        print("Error: Config file not found.")
