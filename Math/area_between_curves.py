"""
A program that will allow the user to input
any two single-variable functions of x and
print the enclosed area between the two
"""

from sympy import Symbol, sympify, Integral, SympifyError


def area(expr1, expr2, var, lower, upper):
    _area = Integral(expr1 - expr2, (var, lower, upper)).doit()
    return _area


if __name__ == "__main__":
    try:
        expr1 = sympify(input("Enter the upper function in one variable: "))
        expr2 = sympify(input("Enter the lower function in one variable: "))
        var = Symbol(input("Enter variable: "))
        lower = float(input("Enter lower bound of the enclosed region: "))
        upper = float(input("Enter upper bound of the enclosed region: "))
    except SympifyError:
        print("Invalid input")
    else:
        result = area(expr1, expr2, var, lower, upper)
        if result:
            print("Area enclosed by {} and {} is equals to: {:.2f}".format(expr1, expr2, result))
