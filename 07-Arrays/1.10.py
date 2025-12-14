#The array contains the student's test results. 
# A value of True indicates that the student answered the question correctly, while a value of False indicates an incorrect answer. 
# Write a program that prints information about the test results:

#Number of questions:
#Number of correct answers:
#Number of incorrect answers:
#Percentage of correct answers:
###
# Prints test statistics
#
test_results = [
   False, True, False, True, True,
   True, True, False, True, True,
   False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers
correct_answers = 0
for answer in test_results:
   if answer:
      correct_answers += 1

# calculates the number of incorrect answers
...

# calculates the percentage of correct answers
...

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print(f'Number of incorrect answers: {question_number-correct_answers}')
print(f'percentage of correct answers: {correct_answers/question_number*100}')