###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input('input first number:'))
number2 = int(input('input second number: '))
operator = input('enter a symbol of mathematical operation (+, -, *, /): ')

if operator == '+':
    result = number1+number1
elif operator == '-':
    result = number1-number1
elif operator == '*':
    result = number1*number1
elif operator == '/':
    result = number1/number1
else:
    print('you can only type in numbers and (+, -, *, /) symbols')
# print result
print(f'{number1} {operator} {number2} = {result}')