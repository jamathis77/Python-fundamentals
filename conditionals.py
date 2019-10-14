# A conditional resolves to a boolean statement ( True or False)

left = True
right = False

# Equality Operators
left != right   # left and right are not equivalent
left == right   # left and right are equivalent
left is right   # left and right are same identity
left is not right # Left and right are not same identity

age_1 = 23
age_2 = 45

# Comparison Operators
age_1 > age_2   # left is greater than right
age_1 < age_2
age_1 >= age_2 
age_1 <= age_2

# Logical Operators
age_1 == 4 and age_2 < 22   # and operator (True) and (True)
age_1 == 4 or age_2 < 22    # or operator 
not age_1 == 23 

# a         b           a and b
#-------------------------------
# True      True        True
# True      False       False
# False     True        False
# False     False       False

# a         b           a or b
# -----------------------------
# True      True        True
# True      False       True
# False     True        True
# False     False       False

# a         not a
# ---------------
# True      False
# False     True

# x = 3
# name = "Ryan"

# if x > 3 and name == "Ryan":
#     if True:
#         print("I'm inside of an if if statment")
#     print("X is pretty big, and that person's name is ryan")
# elif x <= 3:
#     print("Maybe x is big, idunno")
# else:
#     print("Otherwise, no")

# Challenge
# Take a name and age, and if the person is under 18, say "NAME, you are not an adult",
# if the person is 18 but not 21, say "You are an adult, but not quite yet"
# if the person is 21 and older, say ' You are fully an adult '

# cases ( 12, 18, 20, 21, 89 )

# extra spicy
# If their name starts with an A, say "Cool name"

# name = input("What is your name? > ")
# age = int(input("What is your age? > "))

# if age in range(18):
#     print(f"{ name }, you are not an adult")
# elif age in range(18, 21):
#     print("You are an adult, ish")
# elif age >= 21:
#     print("You are a big person now")

# if name[0].lower() == "a":
#     print("Cool name")



# Declare a number
# If the number is divisible by 3, print "Fizz"
# If the number is divisible by 5, print "Buzz"
# If the number is divisible by both 3 AND 5, print ONLY "FizzBuzz"
# Otherwise, just print the number

# Test cases: 1, 3, 5, 10, 15, 98 

number = 98

if number % 3 == 0 and number % 5 == 0:  # Or number % 15 == 0
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
