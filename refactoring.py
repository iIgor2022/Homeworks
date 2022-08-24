import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailExchange:
    def __init__(self, sender_address, sender_password):
        self._GMAIL_SMTP = "smtp.gmail.com"
        self._GMAIL_IMAP = "imap.gmail.com"

        self.login_address = sender_address
        self.password = sender_password
        self._subject = 'Subject'
        self._header = None

    def send_message(self, recipients, message):
        msg = MIMEMultipart()
        msg['From'] = self.login_address
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = self._subject
        msg.attach(MIMEText(message, 'plain'))

        ms = smtplib.SMTP(self._GMAIL_SMTP, 587)
        # identify ourselves to smtp gmail client
        ms.ehlo()
        # secure our email with tls encryption
        ms.starttls()
        # re-identify ourselves as an encrypted connection
        ms.ehlo()

        ms.login(msg['From'], self.password)
        ms.sendmail(msg['From'], msg['To'], msg.as_string())

        ms.quit()

    def receive_message(self):
        mail = imaplib.IMAP4_SSL(self._GMAIL_IMAP)
        mail.login(self.login_address, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self._header if self._header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == "__main__":
    email_exchange = EmailExchange('login@gmail.com', 'password')
    email_exchange.send_message(['vasya@email.com', 'petya@email.com'], "Message")
    print(email_exchange.receive_message())