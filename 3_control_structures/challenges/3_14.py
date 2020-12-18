import math


def main(a, b ,c):
    if a <= 0 or b <= 0 or c <= 0:
        print("Alle sidene av trekanten må ha positiv verdi")
    else:
        cos_a = (b**2+c**2-a**2) / (2 * b * c)
        print(math.degrees((math.acos(cos_a))))
        cos_b = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
        print(math.degrees((math.acos(cos_b))))
        cos_c = (c ** 2 + a ** 2 - b ** 2) / (2 * a * c)
        print(math.degrees((math.acos(cos_c))))


main(3, 4, 5)