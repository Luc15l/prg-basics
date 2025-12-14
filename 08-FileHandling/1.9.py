###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
def f(file_name):
   job_title = 'Software Engineer'
   liczba=1
   with open(file_name, 'r') as file:
    for line in file:
      if job_title in line:
         print(f'{liczba}. {line.strip()}')
         liczba+=1
f(file_name)