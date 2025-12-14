arr=['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
max=arr[0]
for imie in arr:
    if len(imie)>len(max):
        max= imie
print(max)