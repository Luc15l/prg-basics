def f(amount_to_pay):
    x5 = amount_to_pay//5
    y5 = amount_to_pay - x5*5 
    x2 = y5//2
    y2 = y5 - 2*x2
    

    if y5 == 0 :
        wynik = x5
    elif y2 == 0:
        wynik = x5 + x2
    else:
        wynik = x5 + x2 + y2 
    return wynik
print(f(17))
        