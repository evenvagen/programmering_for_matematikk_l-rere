a = 3

def kvadrer(a):
    b = a*a
    return b


c = kvadrer(kvadrer(a))

print(c)

# a) var a,c (linje 1, 8) = global, var a,b (linje 4) er lokal
# b) 81