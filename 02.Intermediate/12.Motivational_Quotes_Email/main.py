import smtplib
import datetime as dt
import random

now = dt.datetime.now()

# Get quotes
quotes = {}
with open("quotes.txt") as quotes_file:
    for row in quotes_file:
        quote_line = row.split(" - ")
        quotes[quote_line[0]] = quote_line[1]

random_quote = random.choice(list(quotes.keys()))
author = quotes[random_quote]

# Send Quotes
my_email = "kngxtest@gmail.com"
recipient_email = "kevinngx625@gmail.com"
MESSAGE = f"Subject:Motivational Quote\n\n{random_quote}\n{author}"
password = input("Password: ")

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()

connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs=recipient_email,
    msg=MESSAGE)
print("Email succesfully sent")

connection.close


