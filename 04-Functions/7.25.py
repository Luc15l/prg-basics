def f(x,y):
    wynik = 0
    for liczba in range(x, y+1):
        if liczba%2 == 0 and liczba%3 ==0:
            if liczba%4 !=0:
                wynik += liczba
    return wynik

#Define the function f(x,y), which returns the sum of numbers in the range <x,y>
#  that are completely divisible by 2 and 3 and not divisible by 4. Sample result:

print(f(1,20)) #returns 24
print(f(10,30))# returns 48
