a = 3
b = 4


def kvadratrot(a):
    return a ** 0.5


def hypotenus(a, b):
    c = kvadratrot(a ** 2 + b ** 2)
    return c


c = hypotenus(a, b)

print(c)