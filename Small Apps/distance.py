#!/usr/bin/env python3
import math


def distance():
    """Calculates the distance between two points on earth"""
    t1, g1 = input("Enter longitude and latitude for first location: ").split()
    t2, g2 = input("Enter longitude and latitude for second location: ").split()

    t1, g1 = float(t1), float(g1)
    t2, g2 = float(t2), float(g2)

    t1 = math.radians(t1)
    g1 = math.radians(g1)
    t2 = math.radians(t2)
    g2 = math.radians(g2)

    distance = 6371.01 * math.acos(math.sin(t1) * math.sin(t2) + math.cos(t1) * math.cos(t2) * math.cos(g1 - g2))

    print("The distance between these coordinates: {} km".format(round(distance)))


if __name__ == "__main__":
    distance()

    # todo:
    # add map to show locations
    # add ability to enter city name and it finds longitude and latitude
    # add formulas
