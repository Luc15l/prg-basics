def f(number, even):
    wynik = 0
    for litera in str(number):
        cyfra = int(litera)
        if cyfra%2 == 0 and even == True:
            wynik += cyfra
        elif cyfra%2 != 0 and even == False:
             wynik += cyfra
    return wynik
print(f(11111111111111111111111111112, False))
