#Flight numbers along with the number of passengers are stored in a dictionary d. Define a function f(d) that
#returns the number of flights in which the number of passengers is greater than the average number of passengers
#on all flights. Example:
def f(d):
    l=0
    suma=0
    wynik=0
    for nazwa, liczba in d.items():
        suma+= liczba
        l+=1
    srednia =suma/l
    for nazwa, liczba in d.items():
        if liczba>srednia:
            wynik+=1
    return wynik 
print(f({"LO231":150,"BA787":120,"NZ15":30})) # returns 2
print(f({"LO231":150,"BA787":20,"NZ15":30})) # returns 1 