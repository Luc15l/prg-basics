def f(number1,number2,operator):
    if operator == "+":
        wynik = number1 + number2
    elif operator == "%":
        wynik = number1 % number2
    elif operator == "**":
        wynik = number1 ** number2
    elif operator == "*":
        wynik = number1 * number2
    elif operator == "-":
        wynik = number1 - number2
    return wynik
print(f(2,3, "**"))
