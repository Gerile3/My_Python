#!/usr/bin/env python3
import sympy
from sympy.core.relational import Relational, Equality


def i_solver(expr_raw):
    x = sympy.Symbol("x")

    rel = expr_raw.rel_op
    lhs = expr_raw.lhs

    if expr.is_polynomial():
        poly = sympy.Poly(lhs, x)
        return sympy.solve_poly_inequality(poly, rel)

    elif expr.is_rational_function():
        numer, denum = lhs.as_numer_denom()
        p1 = sympy.Poly(numer)
        p2 = sympy.Poly(denum)
        return sympy.solve_rational_inequalities([[((p1, p2), rel)]])

    else:
        return sympy.solve_univariate_inequality(expr_raw, x, relational=False)


if __name__ == "__main__":
    # example expressions: x**2-4<0 , sin(x)-0.8>0, x-2/4>0
    try:
        expr = sympy.sympify(input("Enter an expression to solve: "))
    except sympy.SympifyError:
        print('Invalid input')
    else:
        if isinstance(expr, Relational) and not isinstance(expr, Equality):
            result = i_solver(expr)
            print("for {} expression result is: {}".format(expr, result))
        else:
            print('Invalid inequality')
