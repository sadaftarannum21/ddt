from os import getenv

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Email, Content, To


class SendGridApi:
    """
    SendGridApi is an entity that...
    TODO: documentation for SendGridApi.py
    """

    def __init__(self):
        print(r'SendGridApi')
        self.ApiCall()

    class ApiCall:

        def __init__(self):
            print(r'ApiCall')
            #sg = self.host()
            #hd = self.header(sg)
            #self.request(sg, hd)

        def host(self):
            # TODO: sendgrid.py , incorporate a domain to the project
            return SendGridAPIClient(api_key=getenv('API_KEY_SENDGRID'))

        def header(self, sg):
            # TODO: sendgrid.py , adjust the from * and to * fields for sendgrid
            from_email = Email("test@domain.whatever")
            to_email = To("test@domain.whatever")
            subject = "SUBJECT data from client via SendGrid to email"
            content = Content("text/plain", "CONTENT data from client via SendGrid to email")
            mail = Mail(from_email, to_email, subject, content)
            mail_json = mail.get()
            return mail_json

        def request(self, sg, hd):
            # TODO: sendgrid.py , enhance support for response codes, content types, and pagination
            response = sg.client.mail.send.post(request_body=hd)
            print(response.status_code)
            print(response.headers)
