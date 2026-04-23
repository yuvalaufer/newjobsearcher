import requests
import json
import os
from datetime import datetime

class JobScraper:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

    def scrape_upwork(self, keywords):
        print(f"Searching for music and tech jobs: {keywords}...")
        found_jobs = []
        
        # מקור 1: RemoteOK (חזק בטכנולוגיה, DevOps ו-Python)
        found_jobs.extend(self._search_remote_ok(keywords))
        
        # מקור 2: גירסה מותאמת לחיפוש משרות מוזיקה וקריאייטיב
        # הערה: אתרי מוזיקה כמו SoundBetter סגורים יותר, אז נשתמש ב-API של משרות פרילנסר
        found_jobs.extend(self._search_creative_jobs(keywords))
        
        return found_jobs

    def _search_remote_ok(self, keywords):
        jobs = []
        try:
            url = "https://remoteok.com/api"
            response = requests.get(url, headers=self.headers, timeout=10)
            if response.status_code == 200:
                data = response.json()
                for item in data:
                    # ב-RemoteOK הפריט הראשון הוא בד"כ טקסט משפטי, נדלג עליו
                    if not isinstance(item, dict): continue
                    
                    title = item.get('position', '').lower()
                    desc = item.get('description', '').lower()
                    
                    if any(word.lower() in title or word.lower() in desc for word in keywords):
                        jobs.append({
                            "title": item.get('position'),
                            "platform": "RemoteOK",
                            "link": item.get('url'),
                            "budget": f"{item.get('salary_min', 'N/A')}$ - {item.get('salary_max', 'N/A')}$",
                            "date_posted": datetime.now().strftime("%Y-%m-%d")
                        })
        except: pass
        return jobs

    def _search_creative_jobs(self, keywords):
        # כאן אנחנו משתמשים בחיפוש ממוקד דרך מנוע ה-Jobs של ספקי תוכן
        # בשלב זה הבוט יחפש התאמות למשרות 'Creative' ו-'Transcription' (לתרגום)
        creative_jobs = []
        try:
            # שימוש ב-API של Jobspresso למשרות מגוונות
            url = "https://jobspresso.co/wp-json/wp/v2/job-listings?per_page=50"
            res = requests.get(url, headers=self.headers, timeout=10)
            if res.status_code == 200:
                data = res.json()
                for item in data:
                    title = item.get('title', {}).get('rendered', '').lower()
                    if any(word.lower() in title for word in keywords):
                        creative_jobs.append({
                            "title": item.get('title', {}).get('rendered'),
                            "platform": "Jobspresso",
                            "link": item.get('link'),
                            "budget": "Fixed/Project based",
                            "date_posted": datetime.now().strftime("%Y-%m-%d")
                        })
        except: pass
        return creative_jobs

def save_jobs(jobs, filename):
    if not os.path.exists('data'):
        os.makedirs('data')
    path = f"data/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)
