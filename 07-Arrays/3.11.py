def bubblesort(array):
    i=0
    while i<len(array):
        for j in range(0, len(array)-i-1):
            if array[j]>array[j+1]:
                array[j], array[j+1]= array[j+1], array[j]
        i+=1
    return array

print(bubblesort([5, 2, 9, 1, 5, 6]))
print(bubblesort([10, -3, 0, 8, 7]))
print(([1, 2, 3, 4]))