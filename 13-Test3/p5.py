# A valid number on the planet Metis consists of the digits 1 through 7 
# and the lower or upper case letters athrough d. A plus (+) or minus (-)
#  sign can also appear at the beginning of the number. Create a function
#f(mnumbers) that returns how many numbers in the array mnumbers are valid on the planet Metis. Example:
import re
def f(mnumbers):
    ok= '[+-]?[A-Da-d1-7]+'
    w=0
    for numer in mnumbers:
        if re.fullmatch(ok,numer):
            w+=1
    return w
print(f(["A15","-31","7abC","+D1","-g4"]))# returns 4
print(f(["A05","-3+1","7ab8C","+Bb7","-22c55"]))# returns 2 