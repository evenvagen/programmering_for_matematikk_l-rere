from math import sqrt

a = float(input("Lengde på katet a: "))
b = float(input("Lengde på katet b: "))

hypotenuse = round(sqrt(a**2 + b**2), 2)

print(hypotenuse)