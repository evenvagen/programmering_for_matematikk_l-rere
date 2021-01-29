i = 0
correct_answers = 0
answer = ''

while i < 20 and (answer != 'x'):
    i += 1
    print(f"Hva er {i} * {i}?")
    answer = input("Svar: ")
    if answer == str(i ** 2):
        correct_answers += 1
        print(f"Korrekt, så langt har du {correct_answers} riktig")
    elif answer == 'x':
        print("Velkommen tilbake")
    else:
        print(f"feil svar, riktig er {i ** 2}")


if correct_answers == 20:
    print("Meget bra")
else:
    print("Ta en pause, kom tilbake, og prøv igjen")