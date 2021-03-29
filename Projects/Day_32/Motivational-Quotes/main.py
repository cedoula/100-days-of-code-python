import datetime as dt
from random import choice
import smtplib
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

from email_info import my_email, password

with open("quotes.txt", "r") as quotes_file:
    quotes = quotes_file.readlines()

now = dt.datetime.now()
current_day = now.weekday()
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

