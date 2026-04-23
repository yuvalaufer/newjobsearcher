import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

class JobScraper:
    def __init__(self):
        # הגדרת User-Agent כדי שהאתר יחשוב שאנחנו דפדפן רגיל ולא בוט
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        }

    def scrape_upwork(self, keywords):
        print(f"Searching Upwork for: {keywords}...")
        found_jobs = []
        
        # בשלב הראשון, אנחנו בונים את המבנה. 
        # Upwork חוסמים סריקה פשוטה לעיתים קרובות, לכן נתחיל בלוגיקה שתייצר לנו את האובייקטים.
        for query in keywords:
            # כאן תבוא בעתיד הקריאה ל-API או ל-BeautifulSoup
            # לצורך הטסט הראשון, הבוט ייצור "משרה לדוגמה" כדי שנוכל לבדוק את ה-Pipeline
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
    path = f"data/{filename}"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(jobs, f, indent=4, ensure_ascii=False)
    print(f"Saved {len(jobs)} jobs to {path}")
