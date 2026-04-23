import os
import sys

# שורות קריטיות להרצה ב-GitHub Actions:
# מוודא שהסקריפט מזהה את התיקייה שבה הוא נמצא כדי לייבא את scraper ו-notifier
sys.path.append(os.path.dirname(__file__))

from scraper import JobScraper, save_jobs
from notifier import send_job_email

def main():
    # אתחול הסורק
    scraper = JobScraper()
    
    # 1. הגדרת מילות החיפוש עבור הבוט המוזיקלי
    music_keywords = [
        "piano recording", "session pianist", 
        "vocal harmonies", "backing vocals", "song translation"
    ]
    
    print("Starting Music Job Bot...")
    music_jobs = scraper.scrape_upwork(music_keywords)
    
    # שמירת התוצאות לקובץ JSON בתיקיית data
    save_jobs(music_jobs, "music_jobs.json")
    
    # 2. שליחת אימייל לעצמך
    my_email = os.getenv("EMAIL_USER")
    
    if music_jobs and my_email:
        print(f"Attempting to send email to {my_email}...")
        send_job_email(my_email, music_jobs)
    else:
        print("No jobs found or email (EMAIL_USER) not configured in Secrets.")

if __name__ == "__main__":
    main()
