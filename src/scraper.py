import requests
import json
import os
from datetime import datetime

class JobScraper:
    def __init__(self):
        # שימוש ב-User-Agent כדי להיראות כמו דפדפן אמיתי
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

    def scrape_upwork(self, keywords):
        print(f"Searching for real jobs: {keywords}...")
        found_jobs = []
        
        # אנחנו משתמשים ב-API חופשי של אתר Jobspresso או מנוע חיפוש משרות דומה
        # לצורך הדוגמה האופרטיבית, נשתמש בחיפוש דרך אתר שמגיב טוב לבוטים:
        base_url = "https://remoteok.com/api"
        
        try:
            response = requests.get(base_url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                all_remote_jobs = response.json()
                
                # סינון המשרות לפי מילות המפתח שלך
                for job in all_remote_jobs:
                    # בודקים אם אחת ממילות המפתח מופיעה בכותרת או בתיאור
                    title = job.get('position', '').lower()
                    description = job.get('description', '').lower()
                    
                    if any(word.lower() in title or word.lower() in description for word in keywords):
                        found_jobs.append({
                            "title": job.get('position'),
                            "platform": "RemoteOK",
                            "link": job.get('url'),
                            "budget": f"{job.get('salary_min', 'N/A')} - {job.get('salary_max', 'N/A')}",
                            "date_posted": datetime.now().strftime("%Y-%m-%d")
                        })
            else:
                print(f"Failed to fetch from RemoteOK: {response.status_code}")
        except Exception as e:
            print(f"Error during scraping: {e}")

        # אם לא מצאנו כלום ב-RemoteOK, ננסה עוד מקור (כמו חיפוש ב-GitHub Jobs API חלופי)
        return found_jobs

def save_jobs(jobs, filename):
    if not os.path.exists('data'):
        os.makedirs('data')
    path = f"data/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)
