import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


class info_corona():
    def __init__(self):
        self.url = 'https://www.worldometers.info/coronavirus/'

    def plot(self, context=None):
        """ Plots the latest COVID19 status of the country
            if name is not given then it plots the top10
            example usage: /corona Turkey , /corona """

        response = requests.get(self.url).content
        table = pd.read_html(response, attrs={"id": "main_table_countries_today"})
        df = table[0].fillna(0)
        # df.drop(df.index[0], inplace=True)  # World
        df.drop(["ActiveCases", 'Serious,Critical', 'Serious,Critical', 'Deaths/1M pop', 'Tests/ 1M pop'], axis=1, inplace=True)
        df.drop(df.columns[6], axis=1, inplace=True)

        if len(context) > 3:
            context = context.lower().capitalize()
            df = df.loc[df["Country,Other"] == context]
        if 4 > len(context) > 1:
            context = context.upper()
            df = df.loc[df["Country,Other"] == context]
        if len(context) <= 1:
            df = df[1:]

        C_Names = df["Country,Other"].head(n=10).values.tolist()
        T_Cases = df["TotalCases"].head(n=10).values.tolist()
        # N_Cases = df["NewCases"].head(n=10).values.tolist() # not plotted
        T_Deaths = df["TotalDeaths"].head(n=10).values.tolist()
        # N_Deaths = df["NewDeaths"].head(n=10).values.tolist() # not plotted
        T_Recovered = df["TotalRecovered"].head(n=10).values.tolist()
        T_Tests = df["TotalTests"].head(n=10).values.tolist()

        x = np.arange(len(C_Names))
        width = 0.20

        fig, ax = plt.subplots()

        ax.bar(x - 0.30, T_Cases, width, label='TotalCases', color="Blue")
        ax.bar(x - 0.10, T_Deaths, width, label='TotalDeaths', color="Red")
        ax.bar(x + 0.10, T_Tests, width, label='TotalTests', color="Green")
        ax.bar(x + 0.30, T_Recovered, width, label='TotalRecovered', color="Orange")

        if len(context) > 1:
            ax.set_title("{}'s Situation".format(context))
        else:
            ax.set_title("World's Top10 Situation")

        ax.set_xticks(x)
        ax.set_xticklabels(C_Names)
        ax.legend()
        plt.ticklabel_format(style='plain', axis="y")
        fig.set_size_inches(18.5, 10.5)
        fig.tight_layout()
        plt.grid()

        if len(context) > 1:
            font1 = {'family': 'serif',
                     'color': 'blue',
                     'weight': 'bold',
                     'size': 20}
            font2 = {'family': 'serif',
                     'color': 'red',
                     'weight': 'normal',
                     'size': 20}
            font3 = {'family': 'serif',
                     'color': 'green',
                     'weight': 'normal',
                     'size': 20}
            font4 = {'family': 'serif',
                     'color': 'orange',
                     'weight': 'normal',
                     'size': 20}

            # bbox=dict(facecolor='black', alpha=0.5)
            plt.text(0.863, 0.67, "Total Cases:\n{:,}".format(int(T_Cases[0])), fontdict=font1, transform=ax.transAxes)
            plt.text(0.863, 0.57, "Total Deaths:\n{:,}".format(int(T_Deaths[0])), fontdict=font2, transform=ax.transAxes)
            plt.text(0.863, 0.47, "Total Tests:\n{:,}".format(int(T_Tests[0])), fontdict=font3, transform=ax.transAxes)
            plt.text(0.863, 0.37, "Total Recovered:\n{:,}".format(int(T_Recovered[0])), fontdict=font4, transform=ax.transAxes)

        # plt.savefig('corona.png')  # Uncomment it to save the figure
        plt.show()


if __name__ == "__main__":
    country = input("Enter country or leave blank for World: ")
    test = info_corona()
    test.plot(country)
