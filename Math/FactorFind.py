from sympy import factor, sympify, SympifyError


def factors(num):
    '''Find the factors of an integer'''
    return [i for i in range(1, num + 1) if num % i == 0]


def factors_exp(expr):
    '''Find the factors of an expression'''
    return factor(expr)


if __name__ == '__main__':
    choice = input("1-) Number\n2-) Expression\n>>")

    if choice == "1":
        num = int(input('Enter Number to find factor: '))
        if num > 0:
            print("Factors of {}: {}".format(num, factors(num)))
        else:
            print('Please enter a positive integer')

    elif choice == "2":
        try:
            expr = sympify(input('Enter an expression to factorize: '))
        except SympifyError:
            print('Invalid expression entered as input')
        else:
            print("Factors of ({}): {}".format(expr, factors_exp(expr)))
