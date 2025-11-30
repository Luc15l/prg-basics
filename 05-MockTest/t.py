def f(x, m, y):
    if m == "PM":
        x + 12
    if y > x:
        wynik = y
    else:
        wynik = x
    return wynik
if __name__  == "__main__":
    print(f(8, 'PM', 22))