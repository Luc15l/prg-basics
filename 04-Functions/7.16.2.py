def f(n):
    a, b = 0, 1
    i = 1
    while i < n:
        a, b = b , a + b
        i += 1
    return a
print(f(5))
