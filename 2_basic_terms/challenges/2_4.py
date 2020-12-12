def example():
    ord = "bruttonasjonalprodukt"
    nytt_ord = ord[0:6] + ord[14:21]
    print(nytt_ord)


def challenge():
    name_1 = input("Navn 1: ")
    name_2 = input("Navn 2: ").lower()

    new_word = name_1[0:2] + name_2[0:2]

    print(new_word)


challenge()