def f(palindrome):
    if palindrome == ''.join(reversed(palindrome)):
        wynik =  True
    else:
        wynik = False
    return wynik
print(f("radar"))# returns True
print(f("12-11-21"))# returns True
print(f("book")) # returns False