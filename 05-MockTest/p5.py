def f(binary_number):
    for liczba in binary_number:
        if liczba !='1' and liczba !='0':
            wynik = False
        else:
            wynik = True
    return wynik
print(f('102'))