'''Class which can be used to send emails'''
from collections import namedtuple
import smtplib
import ssl

Credentials = namedtuple('Credentials', 'username password')

class EmailSender:
    def __init__(self, port, smtp_address, credentials, ssl_enabled=False):
        self.port = port
        self.smtp_address = smtp_address
        self.ssl_enabled = ssl_enabled
        self.connection = None
        self.credentials = credentials

    def __enter__(self):
        # Creating a connection to the SMTP server
        if not self.ssl_enabled:
            self.connection = smtplib.SMTP(self.smtp_address, self.port)
        else:
            context = ssl.create_default_context() # if ssl_enabled = True
            self.connection = smtplib.SMTP_SSL(self.smtp_address, self.port, context)

        self.connection.login(self.credentials.username, self.credentials.password)

        return self

    def sendmail(self, sender, reciver, message):
        # Method to send email message
        self.connection.sendmail(sender, reciver, message.as_string())

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
