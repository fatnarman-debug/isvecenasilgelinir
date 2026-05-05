import json
import os

class Sentinel:
    def __init__(self, config_path):
        with open(config_path, 'r') as f:
            self.config = json.load(f)
        
    def scan(self):
        print(f"Starting scan for {self.config['system_name']}...")
        results = []
        for inst in self.config['institutions']:
            print(f"Checking {inst['name']}...")
            # Simulate finding a new item
            # In a real scenario, we'd use requests/beautifulsoup or Ruflo's web tool
            results.append({
                "institution": inst['name'],
                "status": "Scanning (Demo Mode)",
                "url": inst['url']
            })
        return results

if __name__ == "__main__":
    config_path = "agents/watchdog_config.json"
    if os.path.exists(config_path):
        sentinel = Sentinel(config_path)
        scan_results = sentinel.scan()
        print(json.dumps(scan_results, indent=2))
