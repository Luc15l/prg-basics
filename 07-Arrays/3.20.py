arr = [7,9,2,4,5,6]
parz=[]
nparz=[]
for x in arr:
    if x%2==0: parz.append(x)
    else: nparz.append(x)
wynik = parz+nparz
print(wynik)