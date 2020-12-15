import math

a = float(input("Hva er arealoverflaten på kula? "))

r = math.sqrt(a / (4 * math.pi))

v1 = (1/3) * 4 * math.pi * r ** 2 * r

v2 = (4/3) * math.pi * r ** 3

print(F"Kulens volum er {v1}/{v2}, radius er {r}")