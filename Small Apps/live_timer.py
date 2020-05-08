#!/usr/bin/env python3
from datetime import datetime


def alive(date):
    """Function to see for how much time have passed since you have been born"""
    date = date.split("/")

    if len(date) == 3:
        today = datetime.now()
        birthday = datetime(year=int(date[2]), month=int(date[1]), day=int(date[0]))

        year = today.year - birthday.year
        month = today.month - birthday.month
        day = today.day - birthday.day

        if month < 0:
            year = year - 1
            month = abs(today.month - birthday.month)

        if day < 0:
            month = month - 1
            day = abs(today.day - birthday.day)

        months = year * 12 + month
        days = (today - birthday).days
        hours = days * 24 + today.hour
        mins = hours * 60 + today.minute
        seconds = mins * 60 + today.second

        alive = "You are alive for {} years, {} months, {} days!".format(year, month, day)
        alive2 = "In detail thats like:\n {} months\n {} days\n {} hours\n {} mins\n {} seconds".format(months, days,
                                                                                                        hours, mins,
                                                                                                        seconds)

        print(alive, alive2)


if __name__ == "__main__":
    date = input("Enter your birthday (day/month/year): ")
    alive(date)
