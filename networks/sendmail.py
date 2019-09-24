import smtplib, ssl
from email.mime.text import MIMEText
from getpass import getpass

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "dttvn0010@gmail.com"
receiver_email = "duongthanhtungvn01@gmail.com"

password = getpass('Enter your password: ')
print(password)

message = """
       Sample Email sent by Python.
       """

msg = MIMEText(message)
msg['to'] = receiver_email
msg['Subject'] = 'Python send mail test program'

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
   server.login(sender_email, password)
   server.sendmail(sender_email, receiver_email, msg.as_string())