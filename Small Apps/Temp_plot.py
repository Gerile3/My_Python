#!/usr/bin/env python3

import matplotlib.pyplot as plt
from pyowm import OWM


def temp_plot(city):
    """ Plot 5 day weather forecast for the given city"""

    API_key = 'Api key here'  # You can get one free from: https://openweathermap.org/appid
    owm = OWM(API_key)
    fc = owm.three_hours_forecast(city)
    f = fc.get_forecast()
    weather_lst = f.get_weathers()

    weather_days = [weather_lst[i] for i in range(0, len(weather_lst), 8)]
    temps = [i.get_temperature(unit='celsius')['temp'] for i in weather_days]
    dates = [i.get_reference_time(timeformat='iso').split(" ")[0] for i in weather_days]

    plt.plot(dates, temps, marker='o')
    plt.title('Average daily temperature in {}'.format(city))
    plt.xlabel('Day')
    plt.ylabel('Temperature °C')
    plt.axis(ymin=0, ymax=30)
    plt.show()


if __name__ == '__main__':
    # Todo support multiple city plots
    # Todo more informative plots
    city_name = input("Enter city name: ")
    temp_plot(city_name)
