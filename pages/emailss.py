# pages/email_sender.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
from Utilities.helper import get_latest_billing_screenshot
from dotenv import load_dotenv
import os
# Load the .env file
load_dotenv()

class EmailSender:
    def __init__(self):
        # Email configuration from Env
        self.from_address = os.getenv("EMAIL_FROM")
        self.to_address = os.getenv("EMAIL_TO")
        self.subject = os.getenv("EMAIL_SUBJECT")
        self.body = os.getenv("EMAIL_BODY")
        self.screenshot_folder = r"pages\screenshot"

        # SMTP server config (Gmail)
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587
        self.smtp_password = os.getenv("EMAIL_STM_PASSWORD") # App password

    def _attach_screenshot(self, msg):
        """
        Finds the latest screenshot containing 'AWS Billing' and attaches it to the email.
        """
        filename = get_latest_billing_screenshot(self.screenshot_folder)
        if not filename:
            print("❌ No valid screenshot found. Email will not be sent.")
            return False

        with open(filename, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(filename)}')
            msg.attach(part)

        print(f"✔ Attached screenshot: {filename}")
        return True

    def send_email(self):
        """
        Sends the email with subject, body, and latest screenshot.
        """
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = self.from_address
        msg['To'] = self.to_address
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.body, 'plain'))

        # Attach screenshot
        attached = self._attach_screenshot(msg)
        if not attached:
            return

        # Send email via SMTP
        try:
            server = smtplib.SMTP(self.smtp_server, self.smtp_port)
            server.starttls()
            server.login(self.from_address, self.smtp_password)
            server.send_message(msg)
            server.quit()
            print("✅ Email sent successfully.")
        except Exception as e:
            print(f"❌ Failed to send email: {e}")
