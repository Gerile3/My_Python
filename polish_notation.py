# ((15 ÷ (7 − (1 + 1))) × 3) − (2 + (1 + 1))  == 15 7 1 1 + − ÷ 3 × 2 1 1 + + −
# Write a program to make above statement true


operator = "+,-,*,/"


def plus(a, b):
    return a+b


def minus(a, b):
    return a-b


def multi(a, b):
    return a*b


def divide(a, b):
    if b != 0:
        return a/b
    else:
        pass


task = "15711+−÷3×211++−"
