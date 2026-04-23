import os
import json
import sys

# מוסיף את התיקייה הנוכחית (src) לנתיב החיפוש של פייתון
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# עכשיו הייבוא אמור לעבוד בלי בעיה
try:
    from scraper import JobScraper, save_jobs
    from notifier import send_job_email
    print("Imports successful!")
except ImportError as e:
    print(f"Import failed: {e}")
    # הדפסת הקבצים בתיקייה כדי שנבין מה קורה אם זה נכשל
    print(f"Files in src: {os.listdir(current_dir)}")
    sys.exit(1)

def main():
    scraper = JobScraper()
    
    # מילות חיפוש (מוזיקה)
    music_keywords = [
        "piano recording", "session pianist", 
        "vocal harmonies", "backing vocals", "song translation"
    ]
    
    print("Starting Music Job Bot...")
    music_jobs = scraper.scrape_upwork(music_keywords)
    
    # שמירה
    save_jobs(music_jobs, "music_jobs.json")
    
    # שליחת אימייל
    my_email = os.getenv("EMAIL_USER")
    if music_jobs and my_email:
        send_job_email(my_email, music_jobs)
    else:
        print("No jobs found or email not configured.")

if __name__ == "__main__":
    main()
