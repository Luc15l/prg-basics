def f(aar1, aar2):
    for rzecz in aar1:
        if rzecz not in aar2:
            return False
    return True
print(f([1,2,3,4],[1,2,3,4,5,8,9]))
print(f([1,2,3,4,7],[1,2,3,4,5,8,9]))