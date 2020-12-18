def letter_price():
    weight_of_letter = int(input("Hvor mye veier brevet? "))
    if weight_of_letter < 20:
        print("Det vil koste 16kr å sende brevet")
    elif weight_of_letter < 50:
        print("Det vil koste 23kr å sende brevet")
    elif weight_of_letter < 100:
        print("Det vil koste 26 kr å sende brevet")
    else:
        print("Det vil koste 42 kr å sende brevet")


def repeat_function(x_times):
    for i in range(x_times):
        letter_price()


repeat_function(5)

