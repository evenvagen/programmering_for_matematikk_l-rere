def discount(amount, price):

    price_to_pay = amount * price

    if amount <= 100:
        print(price_to_pay)
    elif amount <= 200:
        print(price_to_pay * 0.9)
    elif amount <= 300:
        print(price_to_pay * 0.8)
    else:
        print(price_to_pay * 0.7)


discount(250, 100)