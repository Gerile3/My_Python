from sympy import Symbol, Derivative, sympify, pprint


def derivative_calc(expr, var):
    var = Symbol(var)
    derivative = Derivative(expr, var).doit()
    pprint(derivative)


if __name__ == "__main__":
    try:
        expr = sympify(input("Enter an expression to calculate: "))
        var = input("Enter the variable to differentiate with respect to: ")
    except Exception as err:
        print("Invalid input", err)
    else:
        derivative_calc(expr, var)

# todo : command line version
