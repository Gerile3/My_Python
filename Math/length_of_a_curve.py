"""A program that will calculate the length of a curve between two points"""

from sympy import Derivative, Integral, Symbol, sqrt, SympifyError, sympify


def find_length(expr, var, lower, upper):
    deriv = Derivative(expr, var).doit()
    length = Integral(sqrt(1 + deriv**2), (var, lower, upper)).doit()
    return length


if __name__ == '__main__':
    try:
        expr = sympify(input('Enter a function in one variable: '))
        var = Symbol(input('Enter the variable: '))
        lower = float(input('Enter the lower limit of the variable: '))
        upper = float(input('Enter the upper limit of the variable: '))
    except (SympifyError, ValueError):
        print('Invalid input')
    else:
        print('Length of {} between {} and {} is: {:.2f} '.format(expr, lower, upper, find_length(expr, var, lower, upper)))
