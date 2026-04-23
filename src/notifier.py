import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_job_email(recipient_email, jobs):
    # משיכת פרטי החיבור מה-Secrets של GitHub
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")

    if not sender_email or not sender_password:
        print("Missing email credentials (EMAIL_USER or EMAIL_PASS).")
        return

    # בניית תוכן האימייל
    subject = f"Job Bot: Found {len(jobs)} new opportunities!"
    body = "Hi Yuval, I found some new jobs for you:\n\n"
    
    for job in jobs:
        body += f"- {job['title']} ({job['platform']})\n"
        body += f"  Link: {job['link']}\n"
        body += f"  Budget: {job['budget']}\n\n"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        # חיבור לשרת של גוגל ושליחה
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
