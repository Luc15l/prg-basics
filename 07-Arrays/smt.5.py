wuzek= {
    'chleb':1,
    'maslo':1,
    'woda':6
}
ceny={
    'chleb':5,
    'maslo':4,
    'woda': 3,
    'sok':4,
    'mięso':10
}
def f(wuzek,ceny,pieniądze):
    wynik=0
    for jedzenie,cena in wuzek.items():
        if jedzenie in ceny:
            wynik= ceny[jedzenie]*cena
    if wynik >pieniądze:
        return False
    else:
        return True

print(f(wuzek,ceny,15))