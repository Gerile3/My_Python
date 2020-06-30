"""
implementation of euclid algorithm to find greatest common divisior of two numbers.
With the help of gcd we can also find least common multiple.
Lastly we can implement a diophantine equation solver with the help of gcd.
Todo: Extend functions such that it can accept list of numbers and finds gcd & lcm.
"""


def gcd(a, b):
    """ Find greatest common divisior using euclid algorithm."""
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    return max(a, b)


def extended_gcd(a, b):
    """
    The function extended_gcd(a,b) returns three values: the greatest common divisor of a and b: d=gcd(a,b);
    and two numbers x and y such that d = ax + by
    """
    # assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


def lcm(a, b):
    """
    Least common multiple;
    lcm(a, b) * gcd(a, b) = a * b
    """
    gcd = extended_gcd(a, b)
    result = (a * b) / gcd[0]

    return result


def diophantine(a, b, c):
    """For ax + by = c equation,
    Diophantine equation has a solution (where x and y are integers)
    if and only if c is a multiple of the greatest common divisor of a and b.
    Moreover, if (x, y) is a solution, then the other solutions
    have the form (x + kv, y − ku), where k is an arbitrary integer,
    and u and v are the quotients of a and b (respectively) by the greatest common divisor of a and b.
    For such equation, this function returns x and y solutions.
    """
    gcd = extended_gcd(a, b)
    t = c / gcd[0]
    x_bar = t * gcd[1]
    y_bar = t * gcd[2]

    if a * x_bar + b * y_bar == c:
        return x_bar, y_bar
    else:
        print("No solution")
        return None


def divide(a, b, n):
    assert n > 1 and a > 0 and gcd(a, n) == 1

    d, s, t = extended_gcd(a, n)
    # print([s,t])
    s %= n
    # print(s)
    x = (b * s) % n
    # print(x)
    assert x >= 0
    return x


if __name__ == "__main__":
    print(gcd(0, 10))  # 10
    result = extended_gcd(10, 6)  # 5, 1, -5
    print(result)
    lcm = lcm(42, 35)  # 210 >> 42 x 5 , 35 x 6
    print(lcm)
    dio = diophantine(3, 6, 3)  # 10x + 6y = 14
    print(dio)  # result : for x = -7 and y = 14 we can solve this.
    print(divide(2, 7, 9))
