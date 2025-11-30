def f(password):
    if len(password) >= 6:
        wynik = True
    else:
        wynik = False
    if len(set(password)) == len(password):
        wynik = True
    else:
        wynik = False
    return wynik
print(f("book123"))
print(f("A2water3"))