from math import *

expression = 0

while expression != 'x':
    expression = input("Hva vil du regne ut? (x avslutter programmet): ")
    if expression != 'x':
        print("Resultatet ble: " + str(eval(expression)))


