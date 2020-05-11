#!/usr/bin/env python3
import math
import plotly.graph_objects as go


def plot(coordinates):
    fig = go.Figure(go.Scattermapbox(
        mode="lines+markers",
        lon=coordinates[0],
        lat=coordinates[1],
        marker={'size': 10}))

    fig.update_layout(
        margin={'l': 0, 't': 0, 'b': 0, 'r': 0},
        mapbox={'center': {'lon': 10, 'lat': 10},
                'style': "stamen-terrain",
                'center': {'lon': -20, 'lat': -20},
                'zoom': 1})

    fig.show()


def distance():
    """Calculates the distance between two points on earth"""
    t1, g1 = input("Enter longitude and latitude for first location: ").split()
    t2, g2 = input("Enter longitude and latitude for second location: ").split()
    plot([[t1, t2], [g1, g2]])

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
    # add map to show locations ✔️
    # Show distance in plot as well
    # add ability to enter city name and it finds longitude and latitude
    # add formulas
    # better layout
