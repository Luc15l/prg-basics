###
# BMI Calculator
#
height = input('Wpisz wzrost w cm: ')
weight = input('Wpisz wagę w kg: ')
height = int(height)
weight = int(weight)
bmi = weight / (height/100)**2
bmi = round(bmi,2)
print('Twoje BMI to:', bmi)
if bmi<=18.5:print('Masz niedowagę')
if bmi>18.5 and bmi<25:print('Masz wagę prawidłową')
if bmi>=25:print('Masz nadwagę')