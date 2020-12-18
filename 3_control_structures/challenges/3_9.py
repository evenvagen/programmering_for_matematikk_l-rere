def word():
    word = input("Skriv inn et ord: ")
    if len(word) < 10:
        print("Det var et kort ord")
    elif len(word) < 20:
        print("Det var et mellomlangt ord")
    else:
        print("Imponerende")


word()
