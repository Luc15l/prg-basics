def f(n):
    liczby = str(n)
    wynik = 0
    for liczba in set(liczby):
        ile_razy_się_powtarza = liczby.count(liczba)
        if ile_razy_się_powtarza > 1:
            wynik += int(liczba) * ile_razy_się_powtarza
    return wynik
print(f(513553007))