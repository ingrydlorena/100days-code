'''
Day 79: Automate emails
Automate sending emails using Python
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_servidor = 'smtp.gmail.com'
smtp_porta = 587
user = "your_email"
senha = "your app key"

recipient = ['recipient_email', 'recipient_email', 'recipient_email', 'recipient_email']
msg = MIMEMultipart()
msg['From'] = user
msg['To'] = ", ".join(recipient)
msg['Subject'] = "Day 79 Automate emails"
body = 'Hello World!'
msg.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(smtp_servidor, smtp_porta) as server:
    server.starttls()
    server.login(user, senha)
    server.sendmail(user, recipient , msg.as_string())