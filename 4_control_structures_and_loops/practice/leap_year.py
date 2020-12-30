for i in range(2400, 2450):
    if (i % 4 == 0) and (i % 100 != 0) or (i % 400 == 0):
        print(i)