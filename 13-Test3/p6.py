 #Define a class C that allows you to create objects representing people. The class constructor has 3
#parameters: first name, last name, and age. The text representation of the object contains the initial of the first
#name and last name and the age of the person. If the person age is less than 18 years old, their initials consist of
#lowercase letters, and if they are an adult, they consist of uppercase letters. Example:
def C(f,l,a):
    wynik=''
    wynik= f[0] +l[0]+ str(a)
    if a<18:
        return wynik.upper()
    else: return wynik.lower()
print(C("John","May",21)) #returns "JM21"
print(C("Anna","Brown",17)) #returns "ab17"