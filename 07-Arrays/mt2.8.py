def f(expression):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token.isdigit():      
            stack.append(int(token))
        else:                   
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a-b)
    return stack.pop()
print(f("2 3 +"),
f("2 6 + 4 5 - +") ,
f("11 7 + 15 - 14 +"))