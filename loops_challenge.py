puzzle = open('frequencies.txt', 'r').read().split("\n")
numbers = [ int(i) for i in puzzle ]

# What is the final frequency?

# For loop
# While loop
# Python built-in (goooooooooooogle)

final_step = 0

for each_item in numbers:
    final_step += each_item

print(final_step)


x = 0
total = 0

while x < len(numbers):
    total += numbers[x]
    x += 1

print(total)


built_in = sum(numbers)