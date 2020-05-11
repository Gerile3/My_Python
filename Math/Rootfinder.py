import matplotlib.pyplot as plt


def roots(a, b, c):
    '''Quadratic equation root calculator'''
    D = (b * b - 4 * a * c) ** 0.5
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)
    print('x1: {:.2f}'.format(x_1))
    print('x2: {:.2f}'.format(x_2))
    plt.plot(x_1, x_2, marker='x')
    plt.show()


if __name__ == '__main__':
    print("ax² + bx + c")
    a = input('Enter a: ')
    b = input('Enter b: ')
    c = input('Enter c: ')
    roots(float(a), float(b), float(c))

    x_values = [-1, 1, 2, 3, 4, 5]
    listo = []
    for x in x_values:
        # Calculate the value of the quadratic function
        y = x**2 + 2 * x + 1
        listo.append(y)

    plt.plot(x_values, listo, marker="o")
    plt.show()

    # todo:
    # plot for roots
