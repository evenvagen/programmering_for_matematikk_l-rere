import math

k_0 = float(input("Innskudd: "))
r = float(input("Rentefot (desimalform): "))
n = float(input("Antall år: "))

k_1 = k_0 * (1+r) ** n
k_2 = k_0 * math.e ** (r * n)

annual = round(float(k_2 - k_1),2)
bi_annual = round(k_0 * ((r / 2) + 1) ** (n * 2), 2)
monthly = round(k_0 * ((r / 12) + 1) ** (n * 12), 2)


print(k_1)

print(F"årlig: {annual}\nbi-årlig: {bi_annual}\nmånedtlig: {monthly}")