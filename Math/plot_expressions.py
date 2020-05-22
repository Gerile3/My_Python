#!/usr/bin/env python3
from sympy import Symbol, sympify, SympifyError, solve
from sympy.plotting import plot


def psolve_expressions(expr_1, expr_2):
    '''Plot the graph of input expressions and find solution that satisfies both equations'''
    solution_1y = solve(expr_1, "y")[0]
    solution_2y = solve(expr_2, "y")[0]

    p = plot(solution_1y, solution_2y, ylim=[-10, 10], legend=True, show=False)
    p[0].line_color = "r"
    p[1].line_color = "b"

    p.show()

    com_solution = solve((expr_1, expr_2), dict=True)
    sol_xy = com_solution[0]

    return sol_xy


if __name__ == '__main__':
    try:
        expr_1 = sympify(input('Enter your first expression in terms of x and y: '))
        expr_2 = sympify(input('Enter your second expression in terms of x and y: '))
    except SympifyError:
        print('Invalid input')
    else:
        x = Symbol('x')
        y = Symbol('y')
        solutions = psolve_expressions(expr_1, expr_2)
        print("Solution for expr1({}) and expr2({}): x={}, y={}".format(expr_1, expr_2, solutions[x], solutions[y]))
