import numer
n = 7
x = 2
y = 15
z = numer.dziedzina(n,x,y)
o = ""
if z == True:
    o = "yes"
elif z == False:
    o == "no"
print(f'A number: {n}')
print(f'Number 7 in the range <{x},{y}>: {o}')
