def f(student1, student2):
    suma1 = 0
    licznik1 = 0
    for x in student1.split(","):
        suma1 += int(x)
        licznik1 += 1
    art1 = suma1 / licznik1

    suma2 = 0
    licznik2 = 0
    for x in student2.split(","):
        suma2 += int(x)
        licznik2 += 1
    art2 = suma2 / licznik2

    return art1 if art1 > art2 else art2



if __name__  == "__main__":
    print(f("3,4,5","4,3"))
    print(f("3,4,5","5,5,4,5"))
    print(f("3,4,5,4","4,4"))