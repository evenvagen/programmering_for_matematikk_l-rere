def main():
    age_1 = int(input("Alder på første person? "))
    age_2 = int(input("Alder på andre person? "))
    if age_1 == age_2:
        print("Dere er like gamle")
    else:
        print("Dere har forskjellig alder")


def main_alternative():
    age_1 = int(input("Alder på første person? "))
    age_2 = int(input("Alder på andre person? "))
    if age_1 != age_2:
        print("Dere har forskjellig alder")
    else:
        print("Dere er like gamle")


main_alternative()



