# import smtplib

# my_email = "cedric.vanza@gmail.com"
# password = "4RJM)v56RU1%rG"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     #Encrypt email
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email, 
#         to_addrs="cedric.vanza@yahoo.com", 
#         msg="Subject:Hello\n\nThis is the body of my email."
#     )

import datetime as dt
from random import choice
import smtplib

my_email = "cedric.vanza@gmail.com"
password = "4RJM)v56RU1%rG"

with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()

now = dt.datetime.now()
current_day = now.weekday()
print(current_day)
if current_day == 0:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        #Encrypt email
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="cedric.lutonda@gmail.com", 
            msg=f"Subject:Motivational Quote\n\n{choice(quotes)}"
        )
        print("Email sent.")

