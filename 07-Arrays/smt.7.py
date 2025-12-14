def f(karty):
    wynik=0
    for karta in karty:
        if karta in 'AKQJT':
            wynik+=10
        elif karta.isdigit():
            wynik+=int(karta)
    return wynik

print(f("AJ972"))