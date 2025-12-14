# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
food=0
transport=0
utilities=0
suma=0

# Use loop statements
for week in monthly_expenses:
    food += week[0]
    transport+=week[1]
    utilities+=week[2]
suma+=food + transport+ utilities
# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',food)
print('Transport:',transport)
print('Utilities:',utilities)
print('Week 1:',sum(monthly_expenses[0]))
print('Week 2:',sum(monthly_expenses[1]))
print('Week 3:',sum(monthly_expenses[2]))
print('Week 4:',sum(monthly_expenses[3]))
print('---------------')
print('TOTAL:',suma)