def f(n):
    a, b = 0, 1
    while a <= n:
        if a==n:
            return  True
        a, b = b , a + b
    return False
print(f(1))
        
