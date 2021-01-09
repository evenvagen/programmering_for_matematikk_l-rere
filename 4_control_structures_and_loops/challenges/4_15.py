shopping_list = []

while True:
    item = input(": ")
    if item != 'x':
        shopping_list.append(item)
    else:
        break

print(shopping_list)