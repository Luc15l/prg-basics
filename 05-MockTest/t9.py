def f(size1,size2):
    S = 1
    M = 2
    L = 3
    if size1 == "S":
        size1 = S
    elif size1 == "M":
        size1 = M
    else:
        size1 = L
    if size2 == "S":
        size2 = S
    elif size2 == "M":
        size2 = M
    else:
        size2 = L
    if size1>size2:
        wynik = 1
    elif size1<size2:
        wynik = 2
    else:
        wynik = 0
    return wynik 
if __name__  == "__main__":
    print(f("L","S"))
    print(f("M","L"))
    print(f("S","S"))
    print(f("S","L"))
    print(f("M","S"))