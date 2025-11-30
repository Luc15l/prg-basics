def f(card_number):
    a = str(card_number)
    x1 = a[0:2]
    b = len(a) - 6
    x3 = a[-4:]
    return x1 + b*'*' + x3
print(f(5209312400019022))