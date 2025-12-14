def f(subjects):
    """Zwraca nazwę przedmiotu z najwyższą średnią ocen."""
    wynik = None
    best_avg = 0
    for subj, grades in subjects.items():
        avg = sum(grades) / len(grades)
        if avg > best_avg:
            wynik = subj
            best_avg = avg
    return wynik

if __name__ == "__main__":
    print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]}))  # -> "comp"