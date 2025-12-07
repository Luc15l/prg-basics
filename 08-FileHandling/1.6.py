with open("countries.txt", "r") as file:
    liczba = 1
    for line in file:
        print(f"{liczba}. {line.strip()}")
        liczba += 1
