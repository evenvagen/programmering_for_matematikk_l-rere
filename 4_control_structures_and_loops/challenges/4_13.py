from turtle import *


def stippled_line_a():
    for i in range(0, 10):
        forward(10)
        penup()
        forward(10)
        pendown()
    done()


def heart_rate_b():
    for i in range(0, 10):
        forward(20)
        right(75)
        forward(6)
        left(150)
        forward(16)
        right(150)
        forward(10)
        left(75)
    forward(20)
    done()


def star_c():
    for i in range(9):
        forward(100)
        right(160)
        forward(50)
    done()


def vortex_d():
    for i in range(0, 40, 2):
        circle(i)
    done()


star_c()







