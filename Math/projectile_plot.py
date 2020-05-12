#!/usr/bin/env python3
'''Draw the trajectory of a body in projectile motion'''

import matplotlib.pyplot as plt
import math


def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('Horizontal Distance')
    plt.ylabel('Vertical Distance')
    plt.title('Projectile motion of a ball')


def frange(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    return numbers


def draw_trajectory(ctx):
    u, theta = ctx
    theta = math.radians(theta)
    g = 9.8
    # Time of flight
    t_flight = 2 * u * math.sin(theta) / g
    # Find time intervals
    intervals = frange(0, t_flight, 0.001)
    # List of x and y coordinates
    x = []
    y = []
    for t in intervals:
        x.append(u * math.cos(theta) * t)
        y.append(u * math.sin(theta) * t - 0.5 * g * t * t)
    draw_graph(x, y)


if __name__ == '__main__':
    listo = []
    try:
        plot_number = int(input("Enter the number of plots: "))
        for i in range(1, plot_number + 1):
            u = float(input(f'Enter the initial velocity (m/s) for trajectory {i}: '))
            theta = float(input(f'Enter the angle of projection (degrees) for trajectory {i}: '))
            listo.append((u, theta))
    except ValueError:
        print('You entered an invalid input')
    else:
        for i in range(plot_number):
            draw_trajectory(listo[i])
        plt.legend([f"trajectory {i}" for i in range(1, plot_number + 1)])
        plt.show()

    # to do:
    # ask user how many plots wanted to make (for comprasion between different values) ✔️
    # add max points for plots ❌
    # add formulas as comment ❌
    # add examples ❌
