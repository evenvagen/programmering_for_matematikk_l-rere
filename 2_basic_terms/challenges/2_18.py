import math

a = float(input("Lengde katet a: "))
c = float(input("Lengde hypotenus: "))

b = round(math.sqrt(c**2 - a ** 2), 2)

print(b)