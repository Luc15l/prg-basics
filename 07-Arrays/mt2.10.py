def f(arr):
    b=10
    for wiersz in arr:
        for liczba in wiersz:
            if liczba<b:
                b=liczba
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==b:
                r=i
                c=j
    return c==r
print(f([[7,8],[5,3],[9,4]]))  # 3, row 1, col 1
print(f([[7,8,5,3],[9,4,2,6]]))  # 2, row 1, col 2 