# class A:

#     def one(self):
#         print("I am base class")


# class B(A):
#     def two(self):
#         super().one()
#         print("i am dereived from  Base Class")


# class C(B):
#     def three(self):
#         super().two()
#         print("I am derived from Derived Class")


# obj = C()
# obj.three()


# Base Class
class Animal:
    def sound(self):
        print("i am base class")


class Dog(Animal):
    def tone(self):
        super.tone()
        print("Woof!")


class BullDog(Dog):
    def loud(self):
        super.tone()
        print("Bark")


obj = BullDog()
print(obj.sound())
