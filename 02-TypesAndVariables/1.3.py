###
# BMI Calculator
#
height = input('Enter your height in cm: ')
weight = input('Enter your weight in kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Your BMI is', bmi)
if bmi<=18.5:print('masz niedowagę')
if bmi>18.5 and bmi<25:print('masz wagę prawidłową')
if bmi>=25:print('masz nadwagę')