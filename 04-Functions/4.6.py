###
# Function that returns the full name of a day of the week
# based on its number
#
def day_name(day_number):
    result = ''
    if day_number == 1:
        result = 'poniedziałek'
    elif day_number == 2:
        result = "wtorek"
    elif day_number == 3:
        result = "środa"
    elif day_number == 4:
        result = "czwartek"
    elif day_number == 5:
        result = "piątek"
    elif day_number == 6:
        result = "sobota"
    elif day_number == 7:
        result = "niedziela"
    return result

# Function usage
print('The name of day 5 in the week is', day_name(5))
print('The name of day 3 in the week is', day_name(3))
print('The name of day 7 in the week is', day_name(7))