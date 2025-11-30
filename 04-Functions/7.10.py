def f(x,y):
    a = 0
    for number in range(x,y):
        if number < 0 and number%2==0:
            a += 1
    return a
print(f(-7,8))