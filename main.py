"""Auto email sender"""
import email
from datetime import date
from os import getenv
import sqlite3
from string import Template
from dotenv import load_dotenv
from borowers import get_borowers_by_date
from emails import EmailSender, Credentials

todays_date = date.today()

# Loading environmental variables from .env file
load_dotenv()

# Connection with database
connection = sqlite3.connect(getenv('DB_NAME'))

# Email server settings from environmental variables
ssl_enable = getenv('SSL_ENABLE')
port = getenv('PORT')
smtp_server = getenv('SMTP_SERVER')
username = getenv('MAIL_USERNAME')
password = getenv('MAIL_PASSWORD')
subject = getenv('SUBJECT')
sender = getenv('SENDER')

credentials = Credentials(username, password)

def send_reminder_to_borrower(borower):
    #Function which send reminder email to a borrower
    template = Template('''Hello!
    I would like to ask forgiving away my book
    titled $title Return date has 
    passed $book_return_at
    ''')

    text = template.substitute({
        'name': borower.name,
        'title': borower.book_title,
        'book_return_at': borower.book_return_at
    })

    # Create email message object and set its properties
    message = email.message_from_string(text)

    message.set_charset('utf-8')
    message['From'] = sender
    message['To'] = borower.email
    message['Subject'] = subject
    connection.sendmail(sender, borower.email, message)

    print(f'I sending email to {borower.email}')

if __name__ == "__main__":
    # List of borrowers who need a reminder email today
    borowers = get_borowers_by_date(connection, todays_date)
    # Connecting to the server and sending an email
    with EmailSender(port, smtp_server, credentials) as connection:
        for borower in borowers:
            send_reminder_to_borrower(borower)
