import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

from conf.config import settings
from utils.logger import logger
from utils.plural_utils import plural_form


@logger
def send_email(filename: str, num_rows: int) -> None:
    smtp_username = settings.SMTP_USERNAME
    smtp_password = settings.EMAIL_PASSWORD

    msg = MIMEMultipart()
    msg["To"] = settings.RECIPIENT_EMAIL

    msg["Subject"] = f"В таблица содержится " + plural_form(num_rows)

    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", f"attachment; filename= {filename}")
        msg.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)

        server.send_message(msg)
