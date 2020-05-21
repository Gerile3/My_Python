from sympy import Symbol, pprint


def print_series(n, x_value):
    x = Symbol('x')
    series = x
    for i in range(2, n + 1):
        series = series + (x**i) / i
    pprint(series)

    series_value = series.subs({x: x_value})
    print('Value of the series at {}: {:.2f}'.format(x_value, series_value))


if __name__ == '__main__':
    n = int(input('Enter the number of terms you want in the series: '))
    x_value = float(input('Enter the value of x at which you want to evaluate the series: '))
    print_series(n, x_value)
