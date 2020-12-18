def main():
    print("Dette programmet løser andregradsfunksjoner på formen ax^2 + bx + c")
    a = float(input("a-koeffisenten: "))
    b = float(input("b-koeffisenten: "))
    c = float(input("c-koeffisenten: "))
    if((b**2) - (4*a*c)) > 0:
        x_1 = (-b + (b**2 - 4*a*c) ** 0.5) / (2 * a)
        x_2 = (-b - (b**2 - 4*a*c) ** 0.5) / (2 * a)
        print(F"Løsningen på andregradsligningen er x_1 = {x_1}, x_2 = {x_2}")
    elif ((b ** 2) - (4*a*c)) == 0:
        x_1 = (-b/2*a)
        print(F"Løsningen på andregradsligningen er {x_1}")
    else:
        print("Det finnes ingen reele løsninger")


main()