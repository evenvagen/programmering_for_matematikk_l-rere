number = input("Skriv inn et tall du tror er palindromtall: ")
hits = 0

for i in range(len(number)):
    if number[i] == number[len(number) -i - 1]:
        hits +=1

if hits == len(number):
    print("Palindromtall!")
else:
    print("Ikke palindromtall")