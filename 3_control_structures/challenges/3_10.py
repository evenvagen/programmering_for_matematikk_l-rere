def round(age):
    if age % 10 == 0:
        return F"{age} er et fint og rundt tall"
    else:
        return F"{age} er ikke et rundt tall"


print(round(150))