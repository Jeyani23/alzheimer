import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os

def send_email(receiver_email, patient_name, report_path):
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"  # Use environment variables or secrets in production

    subject = "Your Alzheimer Diagnostic Report"
    body = f"""
    Dear {patient_name},

    Please find attached your Alzheimer diagnostic report. Kindly consult your physician for further interpretation.

    Regards,
    AlzheimerAI Team
    """

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    with open(report_path, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(report_path)}')
        message.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.send_message(message)
    server.quit()
