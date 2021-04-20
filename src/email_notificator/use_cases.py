from dataclasses import dataclass
from email.mime.multipart import MIMEMultipart
from smtplib import SMTP
from typing import Optional

from ..shared.use_case import BaseUseCase
from .dto import EmailMessageDTO


@dataclass
class EmailUseCase(BaseUseCase):
    message = MIMEMultipart("alternative")
    mail: EmailMessageDTO
    server: Optional[SMTP] = None
    receiver_mail: Optional[str] = ""

    def run(self, files: tuple[str] = ()):
        self.smtp_login()
        if isinstance(self.mail.receiver_mails, str):
            self.mail.receiver_mails = [self.mail.receiver_mails]
        for receiver_mail in self.mail.receiver_mails:
            self.receiver_mail = receiver_mail
            self.message_create()
            if files:
                for file in files:
                    self.add_attachment(file)
            self.message_send()

    def smtp_login(self):
        self.server = SMTP(self.mail.smtp_server, self.mail.smtp_port)
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.mail.sender_email, self.mail.sender_password)

    def add_attachment(self, filename: Optional[str] = ""):
        """
        Example:
            from email import encoders
            from email.mime.base import MIMEBase


            if filename:
                attachment = MIMEBase(
                    "application",
                    "vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
                attachment.set_payload(open(filename, "rb").read())
                encoders.encode_base64(attachment)
                attachment.add_header(
                    "Content-Disposition",
                    "attachment; filename=articles_with_errors.xlsx",
                )
                self.message.attach(attachment)
        """
        ...

    def message_create(self):
        self.message["Subject"] = self.mail.subject
        self.message["From"] = self.mail.sender_email
        self.message["To"] = self.receiver_mail
        self.message.attach(self.mail.body)
        self.message = self.message.as_string()

    def message_send(self):
        self.server.sendmail(
            self.mail.sender_email, self.receiver_mail, self.message
        )
        self.server.close()
