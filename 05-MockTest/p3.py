def f(name):
    x = name.split()
    y = ''
    for litera in x:
        y = y + litera[0]
    return y
print(f("nie wiem"))