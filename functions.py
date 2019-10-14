# What is a function?

def FUNCTION_NAME_HERE(x):
    print(x)
    # Code Block
    return "some data"

FUNCTION_NAME_HERE('parameter data')
print(FUNCTION_NAME_HERE("Python is cool"))
# something = FUNCTION_NAME_HERE("I'm data")
# print(something)

# multiple parameters


def cash_register(total, tendered):
    """This takes two numbers and compares them"""

    answer = ""
    """ Hey, I exist too """

    if tendered < total:
        answer = "Hey, I need more money"
    elif tendered == total:
        answer = "Have a nice day"
    else:
        answer = "I owe you some money"

    return answer


answer = cash_register(67, 30)
# help(cash_register)
print(answer)


# Default return statement

def combine(x,y,z):
    """
    Takes 3 numbers and prints their sum
    """
    print(x+y+z)
    if x < 0:
        return 12


what_is_this = combine(1, 2, 3)

print(what_is_this)

if combine(12,12,12):
    print("Found none here")


