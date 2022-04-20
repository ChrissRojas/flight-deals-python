import smtplib

import requests
from smtplib import *
from twilio.rest import Client


class NotificationManager:
    TWILIO_SID = "YOUR SID"
    TWILIO_TOKEN = "YOUR TOKEN"
    TWILIO_PHONE = 'YOUR TWILIO NUMBER'

    def __init__(self):
        self.client = Client(self.TWILIO_SID, self.TWILIO_TOKEN)

    def send_message(self, msg: str):
        self.client.messages.create(
            body=msg,
            from_=self.TWILIO_PHONE,
            to="YOUR PHONE NUMBER"
        )

    def send_emails(self, emails, message, link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="email", password="email")
            for email in emails:
                connection.sendmail(from_addr="email",to_addrs=email["email"],
                                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{link}".encode('utf-8'))
                print(email)
