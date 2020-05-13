#!/usr/bin/env python3
import matplotlib.pyplot as plt

"""
A program that creates a bar chart for
easy comparison of weekly expenditures
"""


def get_user_input():
    categories = int(input("Enter the number of categories: "))
    category = []
    money = []

    for i in range(1, categories + 1):
        print(f"For the category {i}:")
        category.append(input("Enter the category name: ").lower().capitalize())
        money.append(int(input("Expenditure: ")))

    bar_plot(category, money)


def bar_plot(labels, data):
    plt.barh(labels, data, align='center')
    # Set the label of each bar
    plt.xlabel('Amount ($)')
    plt.ylabel('Categories')
    plt.title('Weekly Expenditures')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    get_user_input()
    # todo:
    # add ability to save plots so that you can track monthly expenses by adding these
    # static categories ? e.g [School, Travel, Food, House]
