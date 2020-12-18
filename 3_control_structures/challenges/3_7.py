def intermediate_discount(quantity, price):
    if quantity <= 100:
        return quantity * price
    elif quantity <= 200:
        quantity_number = quantity - 100
        discount = quantity_number * price * 0.9
        normal_price = 100 * price
        return discount + normal_price
    elif quantity <= 300:
        quantity_number = quantity - 100
        discount = quantity_number * price * 0.8
        normal_price = 100 * price
        return discount + normal_price
    else:
        quantity_number = quantity - 100
        discount = quantity_number * price * 0.7
        normal_price = 100 * price
        return discount + normal_price


test = intermediate_discount(250, 100)

print(test)