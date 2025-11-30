def f(name):
    x = ""
    y = name.split()
    for i in y:
       x += i[0]
    return x



#A text contains any number of words. Define a function f(name) 
# that returns the acronym (first letters of all words). Sample result:

print(f("Internet of Things"))# returns "IoT"
print(f("For Your Information"))# returns "FYI"
print(f("Python")) #returns "P"