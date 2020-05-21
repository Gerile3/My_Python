from sympy import expand, sympify
from sympy.core.sympify import SympifyError


def product(expr1, expr2):
    '''Product of two expressions'''
    prod = expand(expr1 * expr2)
    print(prod)


if __name__ == '__main__':
    try:
        expr1 = sympify(input('Enter the first expression: '))
        expr2 = sympify(input('Enter the second expression: '))
    except SympifyError:
        print('Invalid input')
    else:
        product(expr1, expr2)
