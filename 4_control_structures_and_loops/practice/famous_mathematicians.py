famous_mathematicians = ['Euler', 'Abel', 'Gauss', 'Cardano']

print(famous_mathematicians[1])

new_name = input("Nytt navn til liste: ")
famous_mathematicians.append(new_name)
print(famous_mathematicians)

for name in famous_mathematicians:
    print(name)

famous_mathematicians[2] = 'mo'
del famous_mathematicians[1]
famous_mathematicians.remove('Euler')

print("\n")

for i in range(0, len(famous_mathematicians)):
    print(famous_mathematicians[i])
