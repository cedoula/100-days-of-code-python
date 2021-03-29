##################### Steps ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
from random import choice
import smtplib

my_email = "cedric.vanza@gmail.com"
password = "4RJM)v56RU1%rG"

#Import birthday csv into dataframe
birthdays_df = pd.read_csv("birthdays.csv")

def send_birthday_email(df):
    #Check if birthday is today
    if df["month"] == dt.datetime.now().month and df["day"] == dt.datetime.now().day:
        #Pick the letter and update it with the person's name
        with open(f"letter_templates/{choice(['letter_1.txt', 'letter_2.txt', 'letter_3.txt'])}", "r") as file:
            letter = file.read()
        letter = letter.replace("[NAME]", df["name"])

        #Send email
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            #Encrypt email
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email, 
                to_addrs=df["email"], 
                msg=f"Subject:It's your Birthday!!!!\n\n{letter}"
            )
        print(f"Birthday email sent to {df['name']}.")
birthdays_df.apply(send_birthday_email, axis=1)
