def f(subject):
    najp="" 
    najo= 0
    for przedmiot, ocena in subject.items():
        srednia =sum(ocena)/len(ocena)
        if srednia>najo:
            najo=srednia
            najp= przedmiot
    return najp

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))