def f(product_code):
    wynik = 0
    suma = int(product_code[1]) + int(product_code[2]) + int(product_code[0])
    reszta = int(suma)%7
    if reszta == int(product_code[3]):
        wynik = True
    else:
        wynik = False
    return wynik
if __name__  == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))