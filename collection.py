# LIST
# List items can be of any type

names = ["Adam", "Justin", "Xzavier"]
students = [
    "The Rock",
    "Charles",
    "The Undertaker",
    "Big Show",
    "Tony Stark",
    6,
    4+1j,
    [
        "nested lists",
        "are cool",
        [
            56
        ]
    ]
]
names[0] = "Potato"
print(names[0])
names.append("Thanos")
print(names[-1])
print(type(students[-1][-1][0]))

names.insert(1, "Debbie")
# print(names)
students.extend(names)

names.pop()
print(names)
print(len(students))
print(len("Python Course"))

students.remove("Tony Stark")
#                   start : stop : step
print(f'the students are {students}')
new_list = students[:3:1]
print(f'the new_list is {new_list}')
reversed_list = students[::-1]
reversed_again = list(reversed(students))
print(reversed_again)

x = [
    12,
    34
]
y = ["yes", "again"]
print(x + ["yes", "again"])
# print(x.)


# Tuples
# Tuples are like lists, except they are IMMUTABLE

my_tuple = (12, 32)
print(my_tuple[0])

my_name = ("Adam", "Jayne")
f_name, l_name = my_name

tuple_names = ("Matthew", "Mark", "Luke", "John", "Judas")
# something = tuple_names[5]
# print(something)

tester = ("John",)
print(tester)


# Sets
#
states = {"Indiana", "Alaska", "Texas"}
states.add(90)
states.remove("Alaska")     # Removes item, error if not there
states.discard("Canada")    # Removes item if there, silently
states.clear()              # Clears the set of all values

print("Indiana" in states)

my_test = {"single item"}
print(type(my_test))


sentence = "Mary had a, little lamb"
list_of_words = sentence.split()
print(list_of_words)
list(sentence)


my_names = ["Wallaby", "Bakersfield", "colGAte", "COcaCOla"]
check = my_names
# remove colgate
# add Crest
# Change cocacola to lowercase
# grab every other item in the list
# Print each name individually

my_names.remove("colGAte")
my_names.append("Crest")
my_names[2] = my_names[2].lower()
print(my_names[1:4:2])
print(my_names[0])
print(my_names[1])
print(my_names[2])
print(my_names[3])
print(check)
