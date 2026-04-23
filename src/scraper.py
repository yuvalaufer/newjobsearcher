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
        print(f"Searching real-time jobs for: {keywords}...")
        found_jobs = []
        
        # חיפוש במנוע המשרות UseMy (מקור טוב למשרות רימוט מגוונות)
        for query in keywords:
            try:
                # שימוש בחיפוש מבוסס מילים באתרים שמאפשרים גישה נוחה
                url = f"https://api.adzuna.com/v1/api/jobs/gb/search/1?app_id=d63a8a9a&app_key=428c05763567885375f4961596a75973&results_per_page=5&what={query}"
                # הערה: אלו מפתחות דמו לבדיקה, אם זה עובד נשאיר אותם
                
                res = requests.get(url, headers=self.headers, timeout=10)
                if res.status_code == 200:
                    data = res.json()
                    for job in data.get('results', []):
                        found_jobs.append({
                            "title": job.get('title'),
                            "platform": "Adzuna / Global",
                            "link": job.get('redirect_url'),
                            "budget": job.get('salary_min', 'N/A'),
                            "date_posted": job.get('created')
                        })
            except:
                continue
                
        return found_jobs

def save_jobs(jobs, filename):
    if not os.path.exists('data'):
        os.makedirs('data')
    path = f"data/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)
