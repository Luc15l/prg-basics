sentence = 'Nie wiem co robię'
result = list(map(lambda x: len(x), sentence.split()))
print(result)