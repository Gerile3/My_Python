#!/usr/bin/env python3
import requests


def horos():
    """Program that prints out given sign's daily horoscope"""
    sign = input("Enter your sign:")

    params = (('sign', sign),
              ('day', 'today'))

    # Source: https://aztro.readthedocs.io/en/latest/
    request = requests.post('https://aztro.sameerkumar.website/', params=params)

    signs = ['aries', 'taurus', 'gemini', 'cancer', 'leo', 'virgo', 'libra',
             'scorpio', 'sagittarius', 'capricorn', 'aquarius', 'pisces']

    if request.status_code == 200:
        data = request.json()

        lucky_time = data['lucky_time']
        description = data['description']
        color = data['color']
        mood = data['mood']
        lucky_number = int(data['lucky_number'])

        result = "{}\n🔮Mood: {}\n🌈Color: {}\n⏰Lucky Time: {}\n🔢Lucky Number: {}".format(description, mood, color, lucky_time, lucky_number)

        print(result)


if __name__ == "__main__":
    horos()
