'''
clase que tiene la responsabilidad de enviar un correo con la data
pasada por parametro
'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class sendEmail(object):

    def __init__(self, fromaddr, toaddr, Subject, body, password):

        self.fromaddr = fromaddr
        self.toaddr = toaddr
        self.Subject = Subject
        self.password = password
        self.body = body

    def sendEmailUser(self):

        msg = MIMEMultipart()
        msg['From'] = self.fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = self.Subject

        msg.attach(MIMEText(self.body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.fromaddr, self.password)
        text = msg.as_string()
        server.sendmail(self.fromaddr, self.toaddr, text)
        server.quit()
