# Classes

class Person:

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def sleep(self):
        print("I sleep")

class Kid:
    
    def blah(self):
        print("I exist too")
    
    def sleep(self):
        print("I also sleep on books")

class Student(Person, Kid):

    counter = 0
    school = "1150 Academy"

    def __init__(self, name, grade, age):
        super().__init__(name, age)
        self.grade = grade
        self.counter = Student.counter
        Student.counter += 1
    

    
    def have_birthday(self):
        self.age += 1

    def greeting(self):
        return f'Hello, my name is { self.name }. I am in grade { self.grade }'
    
    def sleep(self):
        super().sleep()
        super()
        print("I sleep on books")
    
    def change_name(self, new_name):



xzavier = Student("Justin", 8, 3)
xzaver.name = "Xzavier"
print(xzavier.counter)



s1 = Student(0, 1, 3)
s2 = Student(3, 3, 3)
s3 = Student(9,0, 9)
print(s1.counter)
print(s2.counter)


s3.sleep()



# OOP  ( object oriented programming )
# APIE ( 4 pillars of OOP )
# Abstraction - Hiding lower level operations for user friendlines
#             - Dealing with Ideas rather than Pocedure
# Polymorphism - Functions that operate differently depending on the data given
# Inheritence - Bringing data and functionality in from a parent class or object
#               Single Inheritence - Inheriting from one thing
#               Multi-Level Inheritence - Chaining inheritence ( layered )
#               Multiple Inheritence    - Class inherits several other classes
#               Heirarchical Inheritence - When a class is inherited by multiple classes
# Encapsulation - Data and functions that manipulate that data are bundled together.

name = "you"

def modd_name(to_change):
    to_change = "They"
    return to_change

name = modd_name(name)