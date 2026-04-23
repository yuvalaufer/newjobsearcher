import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from scraper import JobScraper, save_jobs
from notifier import send_job_email

def main():
    scraper = JobScraper()
    
    search_queries = [
        "piano recording", "vocal harmonies", "song translation",
        "Linux administrator", "Bash scripting", "Python automation", 
        "DevOps part time", "IT support remote"
    ]
    
    print(f"Starting search for {len(search_queries)} keywords...")
    found_jobs = scraper.scrape_upwork(search_queries)
    
    # שמירה לגיבוי
    save_jobs(found_jobs, "all_jobs.json")
    
    user_email = os.getenv("EMAIL_USER")
    user_pass = os.getenv("EMAIL_PASS")

    # שולח מייל בכל מקרה (ה-notifier כבר יחליט מה לכתוב בפנים)
    if user_email and user_pass:
        print(f"Executing notification process for {user_email}...")
        send_job_email(user_email, found_jobs)
    else:
        print("Email configuration (Secrets) is missing. Cannot send notification.")

if __name__ == "__main__":
    main()
