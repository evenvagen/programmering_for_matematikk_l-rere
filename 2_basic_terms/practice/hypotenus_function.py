from kvadratrot import kvadratrot


def hypotenus(a, b):
    c = kvadratrot((a ** 2) + (b ** 2))
    return c


c = hypotenus(3, 4)
print(c)


