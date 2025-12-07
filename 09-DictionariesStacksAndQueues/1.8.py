price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
for item, price in price_list.items():
    print(item, price)
suma = sum(price_list.values())
print(suma)
for product in price_list:
    price_list[product]= round(price_list[product]*0.9, 2)
for item, price in price_list.items():
    print(item, price)
suma = sum(price_list.values())
print(suma)
