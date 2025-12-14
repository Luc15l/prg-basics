def f(arr):
    l = len(arr)
    for r in range(l):
           rzad= sum(arr[r])
           kolumna = 0
           for i in range(l):
                kolumna += arr[i][r] 
           if rzad!=kolumna:
              return False
    return True
print(f([[3,7,2], [4,2,5], [5,2,1]]))  # True
print(f([[3,7,2], [4,2,5], [9,2,1]]))  # False
