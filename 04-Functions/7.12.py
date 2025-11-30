def f(n):
    if n > 0:
        wynik = '/'.join(['*']* n)
    else:
        wynik = ''
    return wynik
print(f(11))