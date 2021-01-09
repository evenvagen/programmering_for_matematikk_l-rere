digits = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


average = 0

for num in digits:
    average += num

average = average / len(digits)

print(average)