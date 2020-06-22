"""
Horner's Method Example:
Evaluate value of 2x3 - 6x2 + 2x - 1 for x = 3
Input: 2, -6, 2, -1
Input_2: 3
Output: 5
"""


# https://www.wikiwand.com/en/Horner%27s_method
def solve(co_eff, value):
    result = 0

    if "," in co_eff:
        co_eff = co_eff.split(",")
    else:
        co_eff = list(co_eff.split())

    for a in co_eff:
        # b_i = a_i + b_(i+1) * x_0
        result = int(a) + (result * value)

    return result


if __name__ == "__main__":
    co_eff = input("Enter coefficients of the polynomial: ")
    value = int(input("Enter the value you would like to solve polynomial at: "))
    if value and value:
        result = solve(co_eff, value)
        if result:
            print(f"For x={value}, value of polynomial is {result}")
    else:
        print("Wrong input")
