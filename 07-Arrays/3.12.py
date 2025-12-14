def f(arr):
    i=0
    arr2=[]
    while i<len(arr):
      if arr.count(arr[i]) == 1:
           arr2.append(arr[i])
      i+=1
    return arr2
print(f([2,3,2,5,8,1,9,8]))
