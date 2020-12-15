import math


def find_radius(area):
    return math.sqrt(area / math.pi)


circle = find_radius(300)
print(circle)