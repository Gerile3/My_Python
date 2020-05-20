#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt


def read_csv(filename):

    years = []
    population = []
    line = 0

    try:
        with open(filename) as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if line > 0:
                    # Extract only the year from
                    # date
                    year = row[0].split('-')[0]
                    years.append(year)
                    population.append(int(float(row[1])))
                line += 1
        # reverse the lists sice the original data lists the
        # most recent years first
        population.reverse()
        years.reverse()

    except IOError:
        print("File not found or wrong file")

    return population, years


def info(values):
    mean = int(sum(values) / len(values))
    nums = [(number - mean)**2 for number in values]
    variance = sum(nums) / len(values)
    std = variance**0.5

    values.sort()
    if len(values) % 2 == 0:
        n1 = values[(len(values) // 2) - 1]
        n2 = values[len(values) // 2]
        med = (n1 + n2) // 2
    else:
        med = values[len(values) // 2]

    return (mean, variance, std, med)


def plot_pop(population, years):
    plt.plot(years, population)
    plt.title("Population over years")
    plt.xticks(rotation=90)
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.show()


def plot_pop_dif(population, years):
    pop_diff = []
    years_diff = []

    for i, j in zip(range(len(population)), range(1, len(population))):
        pop_diff.append(population[j] - population[i])

    for i, j in zip(range(len(years)), range(1, len(years))):
        years_diff.append(years[j] + "-" + years[i])

    plt.plot(years_diff, pop_diff)
    plt.title("Population difference over years")
    plt.xticks(rotation=90)
    ax = plt.gca()
    ax.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.show()


if __name__ == "__main__":
    # filename = input("Enter the filename(Currently only supports .csv files): ")
    # Population information has to be like this: Date,Value
    #                                             2018-12-31,82319724.0
    filename = "Files\\Turkey_Population.csv"

    p, r = read_csv(filename)
    infos = info(p)

    print("Mean value of the population: {}, variance: {:.2f}, S.Deviation: {:.2f} and Median: {}".format(infos[0],
          infos[1], infos[2], infos[3]))

    choice = input("1-Show Population over years\n2-Show population difference over years\n>>")
    if choice == "1":
        plot_pop(p, r)
    if choice == "2":
        plot_pop_dif(p, r)
    else:
        print("Wrong choice")
