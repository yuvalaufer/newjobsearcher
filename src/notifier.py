import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_job_email(recipient_email, jobs):
    sender_email = os.getenv("EMAIL_USER")
    sender_password = os.getenv("EMAIL_PASS")

    if not sender_email or not sender_password:
        print("Missing email credentials.")
        return

    # יצירת תאריך ושעה בפורמט: DD/MM/YYYY HH:MM
    now = datetime.now()
    timestamp = now.strftime("%d/%m/%Y %H:%M")
    
    # נושא המייל המעודכן לפי הבקשה שלך
    subject = f"yuval job opportounities {timestamp}"
    
    body = f"Hi Yuval, here are the job opportunities found on {timestamp}:\n\n"
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
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(msg)
        print(f"Email sent with subject: {subject}")
    except Exception as e:
        print(f"Failed to send email: {e}")
