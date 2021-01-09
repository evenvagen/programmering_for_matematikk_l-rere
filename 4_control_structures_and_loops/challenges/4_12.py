import turtle


def triangle_a():
    for i in range(0, 3):
        turtle.forward(100)
        turtle.left(120)
    turtle.done()


def square_b():
    for i in range(0, 4):
        turtle.forward(100)
        turtle.left(270)


def rectangle_c():
    for i in range(0, 2):
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)


def pentagon_d():
    for i in range(0, 5):
        turtle.forward(100)
        turtle.left(72)
    turtle.done()


pentagon_d()