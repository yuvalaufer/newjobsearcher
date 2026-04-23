import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import os  # נוסף בשביל ניהול תיקיות

class JobScraper:
    def __init__(self):
        # הגדרת User-Agent כדי שהאתר יחשוב שאנחנו דפדפן רגיל ולא בוט
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

    def scrape_upwork(self, keywords):
        print(f"Searching Upwork for: {keywords}...")
        found_jobs = []
        
        # לוגיקה זמנית ליצירת אובייקטים (לצורך בדיקת המערכת)
        for query in keywords:
            job = {
                "title": f"Need help with {query}",
                "platform": "Upwork",
                "link": f"https://www.upwork.com/search/jobs/?q={query.replace(' ', '%20')}",
                "budget": "Negotiable",
                "date_posted": datetime.now().strftime("%Y-%m-%d %H:%M"),
                "tags": [query, "Remote"]
            }
            found_jobs.append(job)
            
        return found_jobs

def save_jobs(jobs, filename):
    # תיקון: יצירת תיקיית data אם היא לא קיימת בשרת
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Created 'data' directory.")
        
    path = f"data/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)
    print(f"Successfully saved {len(jobs)} jobs to {path}")
