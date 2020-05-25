from sympy import Symbol, pprint, summation


def add_series(expr, num, values):
    """Print addition of series given by user, if values of the terms provided show the result as well"""
    n = Symbol("n")
    series = summation(expr, (n, 1, num))

    if values:
        listo = []

        values = values.split(",")
        for i in values:
            listo.append(tuple(i.split("=")))

        listo = dict(listo)
        series_value = series.subs(listo)
        print("Addition of the series: {}, result: {}".format(series, series_value))

    else:
        pprint(series)


if __name__ == '__main__':
    # expr = a+(n-1)*d
    # num = 3
    # values = a=5,d=4
    expr = input('Enter the nth term of series: ')
    num = int(input('Enter the number of terms you want in the series: '))
    values = input("Enter the variable values(a=3,b=4... etc, leave blank if not desired):")
    add_series(expr, num, values)
