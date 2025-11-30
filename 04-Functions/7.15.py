def f(detector):
    osoba = 0
    for znak in detector:
        if znak == '+':
            osoba += 1
        if znak == '-':
            osoba -= 1
        if osoba >= 3:
            return True
    return False
print(f("+-+++-+---")) # returns True
print(f("+-+-+-+-")) # returns False
print(f("+-++-+--")) # returns False
print(f("+-++-++-+---")) # returns True
