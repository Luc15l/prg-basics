def occurs(number, array):
    i=0
    while i<len(array):
        if array[i]==number:
            return True
        i+=1
    return False
print(occurs(23,[15,38,23]))
print(occurs(6,[7,1,3,8]))