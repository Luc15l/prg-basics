def f(first,last):
    wynik=0
    with open('healthy_lifestyle.txt', 'r') as file:
        for line in file:
            words= line.split()
            for word in words:
                if word.startswith(first) and word.endswith(last):
                    wynik+=1
    return wynik
print(f("a", "d"))