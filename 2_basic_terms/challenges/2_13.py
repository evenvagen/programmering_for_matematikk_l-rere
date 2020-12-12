import math


def find_radius(area):
    x = math.sqrt(area / math.pi)
    print(round(x, 1))


find_radius(78.5)
