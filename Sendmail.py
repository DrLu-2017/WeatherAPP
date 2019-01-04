import smtplib
class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)
        session.ehlo()
        session.starttls()
        session.login(self.email, self.password)
        self.session = session

    def send_message(self, receipient, subject, body):
        ''' This must be removed '''
        msg_receipient = ', '.join(receipient)
        print(msg_receipient)
        headers = [
            "From: " + self.email,
            "Subject: " + subject,
            "To: " + msg_receipient,
            "MIME-Version: 1.0",
           "Content-Type: text/html"]
        headers = "\r\n".join(headers)
        print(headers)
        self.session.sendmail(
            self.email,
            receipient,
            headers + "\r\n\r\n" + body)