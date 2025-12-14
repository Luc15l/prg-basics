def f(arr):
    i=0
    dom = arr[0]
    if arr[1]== arr[2]:
        dom = arr[1]
    while i<len(arr):
        if arr[i] !=dom:
            wynik= arr[i]
        i+=1
    return wynik
print(f([7,7,7,7,7,7,7,4]))