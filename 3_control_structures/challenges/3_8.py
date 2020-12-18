def compare_two(a, b):
    if a > b:
        return a
    else:
        return b


def compare_three(a, b, c, d):
    a = compare_two(a, b)
    b = compare_two(d, c)

    c = compare_two(a, b)

    return c


compare = compare_three(3, 10, 14, 6)

print(compare)