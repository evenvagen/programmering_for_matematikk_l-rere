def main():
    word = ''
    while (word != 'squirrel') and (word != 'x'):
        word = input("Hvordan staves ekorn på engelsk?")
        if word == 'squirrel':
            print("Helt riktig")
        else:
            print("Det er bra du er matematiker")


main()