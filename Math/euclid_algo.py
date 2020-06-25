"""
implementation of euclid algorithm to find greatest common divisior of two numbers.
Todo: Extend functions such that it can accept list of numbers and finds gcd.
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
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


if __name__ == "__main__":
    gcd = gcd(0, 10)  # 10
    print(gcd)
    result = extended_gcd(55, 10)  # 5, 1, -5
    print(result)
