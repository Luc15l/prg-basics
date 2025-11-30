def f(a, b):
    suma = 0
    for liczba in range(a, b+1):
        if liczba%3 == 0:
            suma += liczba
    return suma
if __name__  == "__main__":
    print(f(1,12))