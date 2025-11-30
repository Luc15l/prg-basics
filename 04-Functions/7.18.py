def f(sentence): 
     wynik = ""
     for znak in sentence:
        if znak == " ":
            continue
        wynik += znak
     return wynik
print(f("integrated development environment"))