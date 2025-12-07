wynik = 0
with open('pets.txt',  'r' ) as file:
    for wiersz in file:
        print(wiersz.strip())  # wyświetlenie linii
        słowa = wiersz.split()  # lista słów w linii
        wynik += len(słowa)
print(wynik)