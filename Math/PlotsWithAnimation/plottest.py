from matplotlib import pyplot as plt
from matplotlib import animation

""" Simple circle animation and Circles in Square Plot"""
# Todo:
# P (x, y) > Q (y + 1 − 1.4x2, 0.3x) , Hénon’s Function
# Sierpin´ ski triangle:
# Transformation 1:
# xn+1 = 0.5xn
# yn+1 = 0.5yn
# Transformation 2:
# xn+1 = 0.5xn + 0.5
# yn+1 = 0.5yn + 0.5Drawing Geometric Shapes and Fractals 171
# Transformation 3:
# xn+1 = 0.5xn + 1
# yn+1 = 0.5yn


def create_circle(x=0, y=0):
    circle = plt.Circle((x, y), 0.5, color="b")
    return circle


def draw_square():
    ax = plt.axes(xlim=(0, 6), ylim=(0, 6))
    square = plt.Polygon([(1, 1), (5, 1), (5, 5), (1, 5)], closed=True, color="black")
    ax.add_patch(square)
    y = 1.5
    while y < 5:
        x = 1.5
        while x < 5:
            c = create_circle(x, y)
            ax.add_patch(c)
            x += 1.0
        y += 1.0
    plt.show()


def update_radius(i, circle):
    circle.radius = i * 0.5
    return circle


def create_animation():
    fig = plt.gcf()
    ax = plt.axes(xlim=(-10, 10), ylim=(-10, 10))
    ax.set_aspect('equal')
    circle = create_circle()
    ax.add_patch(circle)
    anim = animation.FuncAnimation(fig, update_radius, fargs=(circle,), frames=30, interval=50, repeat=False)
    plt.title('Simple Circle Animation')
    plt.show()


if __name__ == '__main__':
    create_animation()
    draw_square()
