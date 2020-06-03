"""
A program that will accept a singlevariable function and a value of that variable and check
whether the input function is continuous at the point where the variable
assumes the value input
"""

from sympy import Symbol, sympify, Limit


def is_continuous(epxr, var, value):
    l_limit = Limit(expr, var, value, dir="-").doit()
    r_limit = Limit(expr, var, value, dir="+").doit()
    func_value = expr.subs({var: value})

    if l_limit == r_limit and func_value == l_limit:
        return True
    return False


if __name__ == "__main__":
    try:
        expr = sympify(input("Enter a function in one variable: "))
        var = Symbol(input("Enter the variable: "))
        value = float(input("Enter the point to check the continuity at: "))
    except Exception as err:
        print("Wrong input", err)
    else:
        result = is_continuous(expr, var, value)
        if result:
            print(f"{expr} is continuous at {value}")
        else:
            print(f"{expr} is not continuous at {value}")
