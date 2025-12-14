# Price list
prices = {'milk': 1.49, 'butter': 2.09, 'juice': 1.19, 'bread': 1.99}

# Shopping cart with quantities
cart = {'juice': 3, 'bread': 1, 'milk': 2}

# Calculate total cost
wynik=0
for produkt, cena in cart.items():
    if produkt in cart:
        wynik += prices[produkt]*cart[produkt]
print(wynik)