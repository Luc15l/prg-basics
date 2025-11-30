def f(number1,number2,number3):
    y = max(number1,number2,number3)
    x = min(number1,number2,number3)
    wynik = y - x
    return wynik
print(f(7,4,9)) #returns 5
print(f(2,12,8)) #returns 10
