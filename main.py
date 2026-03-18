import os
import datetime as dt
import pandas as pd
import random
import smtplib

now = dt.datetime.now()
today_year = now.year
today_month = now.month
today_day = now.day
today = (today_month, today_day)

my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")


data = pd.read_csv('birthdays.csv')

birth_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if (today_month, today_day) in birth_dict:
    birthday_person = birth_dict[(today_month, today_day)]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as f:
        content = f.read()
        x = content.replace("[NAME]", birthday_person["name"])



    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_mail, password=password)
        connection.sendmail(from_addr=my_mail,
                            to_addrs=birthday_person["email"],
                            msg=f"Subject: Happy birthday!\n\n{x}")
