import math


def sphere_volume(area):
    r = math.sqrt(area / (4 * math.pi))
    v = (4 / 3) * math.pi * r ** 3

    return round(v, 2)


sphere = sphere_volume(570)
print(sphere)


