import smtplib
import datetime as dt
import random

my_email = "cpcp195@gmail.com"
password = "QweQwe123()"

quotes = []
with open('quotes.txt') as file:
    # for line in file:
    #     quotes.append(line)
    quotes=file.readlines()



now = dt.datetime.now()
day = now.weekday()
if day == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="chintan0539@gmail.com", msg=f"subject:Monday Motivation\n\n{random.choice(quotes)}")

