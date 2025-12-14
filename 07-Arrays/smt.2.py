def f(rpn):
    składniki = rpn.split()
    wynik=[]
    for składnik in składniki:
        if składnik.isdigit():
            wynik.append(int(składnik))
        else:
            b = wynik.pop()            
            a = wynik.pop()
            if składnik== '+':
                wynik.append(a+b)
            elif składnik== '-':
                wynik.append(a-b)
    return wynik.pop()
print(f("2 3 +"),
f("2 6 + 4 5 - +"),
f("11 7 + 15 - 14 +"))