# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("i am parrent")

#     def sound(self):
#         pass


# # Derived class inheriting from Animal


# class Dog(Animal):
#     def sound(self):
#         return "Woof!"

#     print("i am dog i am in child class")


# # Creating an instance of Dog
# dog = Dog("Roccky")
# print(dog.name)
# print(dog.sound())


# Base Class

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
print(x.printname())

class Student(Person):
    pass 
x = Student("Mike", "Jacklin")
print(x.printname())