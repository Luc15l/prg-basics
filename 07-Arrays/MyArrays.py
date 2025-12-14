def second_largest(arr):
    x= sorted(set(arr))
    if len(x)>1:
     return x[-2]
    else:
        return x[0]
def largest_and_smallest_difference(arr):
    x= sorted(set(arr))
    if len(x)>1:
      return x[-1] - x[0]
    else:
        return x[0]
def mediana(arr):
    x= sorted(arr)
    if len(x)%2 !=0:
        return x[(len(x)//2)]
    else:
        return (x[(len(x)//2)-1] + arr[(len(x)//2)])/2
def smallest_and_largest(arr):
    x= sorted(set(arr))
    return [x[0],x[-1]]
def string(arr):
    return "-".join(str(x) for x in  arr)
p=[7,3,8,5,2]
print(second_largest([7,3,8,5,2]), largest_and_smallest_difference([7,3,8,5,2]),   mediana([7,3,8,5,2]))
print(smallest_and_largest(p))
print(string(p))