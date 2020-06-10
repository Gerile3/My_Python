#!/usr/bin/env python3
import smtplib


class Pymail:
    """An app to send emails (using gmail) with python"""
    def __init__(self, gmail, password):
        self.gmail = gmail
        self.password = password
        self.get_message()

    def get_message(self):
        sent_from = self.gmail
        sent_to = input("Enter e-mail you would like to send message: ")
        sent_subject = input("Enter Subject: ")
        sent_body = input("Enter your message: ")

        email_text = "\r\n".join([
                                 "From: {}",
                                 "To: {}",
                                 "Subject: {}",
                                 "",
                                 "{}"
                                 ]).format(sent_from, sent_to, sent_subject, sent_body)

        self.send_email(email_text, sent_to)

    def send_email(self, email_text, sent_to):
        try:
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.ehlo()
            server.login(self.gmail, self.password)
            server.sendmail(self.gmail, sent_to, email_text)
            server.close()

            print('Email sent!')
        except Exception as exception:
            print("Error: %s!\n\n" % exception)


if __name__ == "__main__":
    gmail_user = input("Enter your gmail: ")
    gmail_app_password = input("Enter your Password: ")
    Pymail(gmail_user, gmail_app_password)
