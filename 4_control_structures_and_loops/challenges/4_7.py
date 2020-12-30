print(2)
for i in range(2, 500):
    counter = 0
    for j in range(2, i):
        if i % j != 0:
            counter += 1
        if counter == i-2:
            print(i)
