def discount(quantity, unit_price):
    price = quantity * unit_price
    if quantity > 3:
        print(price * 0.7)
    else:
        print(price)


discount(3, 300)
discount(4, 150)
discount(2, 300)

