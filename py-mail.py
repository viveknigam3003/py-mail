#To Authenticate Gmail to your Python Script and send an email.
import smtplib

session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()
session.login("MAIL_ID", "PASSWORD_OR_APP_PASSWORD")
session.sendmail("SENDER_EMAIL", "RECIEVER_EMAIL", "MESSAGE")




