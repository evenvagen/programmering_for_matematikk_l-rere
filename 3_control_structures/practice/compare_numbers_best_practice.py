def compare_two(a, b):
    if a > b:
        return a
    else:
        return b


def compare_three(a, b, c):
    compare = compare_two(a, b)
    compare = compare_two(compare, c)
    return compare


compare = compare_three(101, 909, 92)

print(compare)
