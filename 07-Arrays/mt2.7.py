import re
def f(arr):
    pattern='[a-z0-9_]'
    i=0
    for haslo in arr:
        if re.match(pattern,haslo):
            i+=1
    return i
print(f(['adadadwa','awsaw2324','ADAD2314','aa_']))