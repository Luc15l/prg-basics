###
# Functions to read any data type from the keyboard
#
def input_string(message):
    x = str(input(message))
    return x

def input_integer(message):
    x = int(input(message))
    return x

def input_real(message):
    x = float(input(message))
    return x

def input_boolean(message):
    x = (input(message))
    if x == 'y':
       x = True
    else:
       x = False
    return x 