from dataclasses import dataclass
from email.mime.text import MIMEText
from typing import Union

from src.config import settings


@dataclass
class EmailMessageDTO:
    subject: str
    body: MIMEText("")  # NOQA
    receiver_mails: Union[str, list]

    smtp_server: str = settings.smtp_server
    sender_email: str = settings.sender_email
    sender_password: str = settings.sender_password
    smtp_port: int = settings.smtp_port
