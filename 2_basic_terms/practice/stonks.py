import math

K_0 = float(input("Innskudd: "))
r = float(input("Rentefot (desimalform): "))
n = float(input("Antall år: "))

annually = K_0 * (1+r) ** n
continuous = K_0 * math.e ** (r * n)
difference = float(continuous - annually)

print(F"Differansen mellom årlig og kontinuerlig forretning er {difference}")