from statistics import median


def is_right_angle(a, b, c):
    h = max([a, b, c])
    k1 = median([a, b, c])
    k2 = min([a, b, c])

    x = (k1 ** 2) + (k2 ** 2)
    y = x ** 0.5
    if y == h:
        print("Trekanten er rettvinklet")
    else:
        print("Trekanten er ikke rettvinklet")


is_right_angle(6, 8, 10)



