def f(n1, n2):
    a, b = 0, 1
    wynik = 0

    while a <= n2:
        if a > n1:
            wynik += a
        a, b = b, a + b

    return wynik

print(f(1, 5))
print(f(6, 21))