import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from os import getenv

from dotenv import load_dotenv
from utils.logger import logger
from utils.plural_utils import plural_form


@logger
def send_email(filename: str, num_rows: int) -> None:
    load_dotenv()
    smtp_host = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = getenv("smtp_username")
    smtp_password = getenv("your_password")

    msg = MIMEMultipart()
    msg["To"] = getenv("recipient_email")

    msg["Subject"] = f"В таблица содержится " + plural_form(num_rows)

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        msg.attach(part)

    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        server.send_message(msg)
