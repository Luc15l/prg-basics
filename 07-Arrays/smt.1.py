arr1= ['rydz', 'pieczarka','kurki']
arr2=['pieczarka', 'grzyb ze ściany']
for grzyb in arr1:
    if grzyb not in arr2:
        arr2.append(grzyb)
print(arr2)