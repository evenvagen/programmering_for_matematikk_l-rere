def biggest_variable(a, b , c):
    if a > b:
        biggest = a
    else:
        biggest = b
    if c > biggest:
        biggest = c
    return biggest


a = biggest_variable(13, 6, 9)

print(a)

