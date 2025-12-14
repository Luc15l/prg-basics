def f(arr):
    wynik=0
    for liczba in arr:
        if liczba%2!=0:
            wynik+=1
    return wynik
print(f([1,2,3,4,5]))