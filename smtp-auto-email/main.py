#Send Motivational qoutes on every Monday
import smtplib
import datetime as dt
import random

MY_EMAIL = "SENDER_EMAIL"
MY_PASSWORD = "SENDER_PASSWORD"
RECEIVER_EMAIL = "RECEIVER_EMAIL"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=RECEIVER_EMAIL ,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

#you need to give access to your gmail account for this.
#you can run it on cloud also with the help of python anywhere
#you can change the day according to you, just change the weekday 