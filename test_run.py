from src.scraper import JobScraper, save_jobs

scraper = JobScraper()
# טסט למשרות מוזיקה
music_keywords = ["piano recording", "vocal harmonies"]
jobs = scraper.scrape_upwork(music_keywords)
save_jobs(jobs, "music_jobs.json")
