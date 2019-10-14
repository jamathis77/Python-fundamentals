# LOOPS
# For loop

animals = ["Jaguar", "Raccoon", "Fox", "Cat", "Toucan"]

for x in animals:
    print(x)

# for number in range(1,101):
#     if number % 3 == 0 and number % 5 == 0:  # Or number % 15 == 0
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


expenses = [
    ("McDonalds", 12.00),
    ("Steam", 49.99),
    ("Rent", 900.00)
]

total = 0.0

for expense in expenses:
    total += expense[1]
    print(total)

print(total)




# While loop

while False:
    #code block
    print("I'm in a while loop")


x = 101

while x < 100:
    print(x)
    x += 4
    if x == 92:
        break
else:
    print("While loop never ran")



products = ["nvidia", "amd", "arm", "intel", "risc"]
search_term = "blah"

# Create a while loop that searches this list until it finds the search term

x = 0

while x < len(products) and search_term != products[x]:
    print(x)
    print(products[x])
    x += 1

if search_term in products:
    print(products.index(search_term))
else:
    print("not found")