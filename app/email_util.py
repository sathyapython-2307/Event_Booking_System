import smtplib
from email.mime.text import MIMEText

def send_email(to_email, subject, content):
    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = "your@email.com"
    msg["To"] = to_email
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("your@email.com", "yourpassword")
        server.send_message(msg)
