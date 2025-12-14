def number(text):
    return len(text.split())
def longest(text):
    words = text.split()
    w2 = sorted(words, key=len, reverse=True)
    return w2
def a(text):
    words = text.split()
    w2 = sorted(words)
    return w2
text = "An apple a day keeps the doctor away"
print(number(text))
print(longest(text))
print(a(text))

