###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
def triangle_area(a,b,c):
    s = 1/2*(a+b+c)
    a =(s*(s-a)*(s-b)*(s-c))**(1/2)
    return a
a1 = triangle_area(3,4,5)
print(f'he area of ​​a triangle with sides ... is {a1}')
a2 =triangle_area(5,12,13)
print(f'he area of ​​a triangle with sides ... is {a2}')  
a3 =triangle_area(7,24,25)
print(f'he area of ​​a triangle with sides ... is {a3}')