sentence = input("Skriv inn en lang setning: ")

encrypted = ""

for i in range(len(sentence)-1, 0, -2):
    encrypted += sentence[i]

print(encrypted)