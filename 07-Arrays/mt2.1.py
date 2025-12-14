def  f(player1,player2):
    suma1=0
    for karta in player1:
        if karta in 'AKQJT':
            suma1+=10
        else:
            suma1+=int(karta)
    suma2=0
    for karta in player2:
        if karta in 'AKQJT':
            suma2+=10
        else:
            suma2+=int(karta)
    if suma1>= suma2:
        return True
    else: return False
print(f("AJ972","AQT72"))
print(f("9532","K8"))