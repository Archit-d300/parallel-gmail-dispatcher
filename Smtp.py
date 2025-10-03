import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "projectemail523@gmail.com"
SENDER_PASSWORD = "mkjk pdzn lljy odwl"

recipients = ["architdeshpande.study@gmail.com", "adarchit.30@gmail.com", "24deshpandea@rbunagpur.in"]

msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = ", ".join(recipients)  
msg["Subject"] = "Group Email Test"

body = """Hello Everyone,

This is an automatically generated group email.
All of you are receiving this in one go.

Regards,
Archit
"""
msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()
    server.login(SENDER_EMAIL, SENDER_PASSWORD)

    server.sendmail(SENDER_EMAIL, recipients, msg.as_string())
    print("Group Email Sent Successfully!")

    server.quit()
except Exception as e:
    print(f"Failed to send email: {e}")
