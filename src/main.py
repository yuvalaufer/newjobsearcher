from scraper import JobScraper, save_jobs
from notifier import send_job_email
import os

def main():
    scraper = JobScraper()
    
    # הגדרת מילות החיפוש עבור הבוט המוזיקלי
    music_keywords = [
        "piano recording", "session pianist", 
        "vocal harmonies", "backing vocals", "song translation"
    ]
    
    # הרצת הסריקה (כרגע לדוגמה)
    print("Starting Music Job Bot...")
    music_jobs = scraper.scrape_upwork(music_keywords)
    
    # שמירה לקובץ
    save_jobs(music_jobs, "music_jobs.json")
    
    # שליחת אימייל לעצמך
    my_email = os.getenv("EMAIL_USER")
    if music_jobs and my_email:
        send_job_email(my_email, music_jobs)
    else:
        print("No jobs found or email not configured.")

if __name__ == "__main__":
    main()
