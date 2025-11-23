###
# Calculates the sum of the digits in a number
#
def sum_digits(number):
    number = abs(number)
    x = 0
    for o in str(number):
        x += int(o)
    return x

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print(f'The sum of the digits in the number {any_number} is {result}')