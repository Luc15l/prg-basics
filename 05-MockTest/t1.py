import math
def f(obwód):
    średnica = obwód/math.pi
    if średnica >=50:
        wynik = True
    else:
        wynik = False
    return wynik
if __name__  == "__main__":
    print(f(200))
    print(f(100))
