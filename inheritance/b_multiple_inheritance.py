class Animal:
    def make_sound(self):
        pass


class Vehicle:
    def move(self):
        pass


# Derived class inheriting from both animal and vehicle class


class DogCar(Animal, Vehicle):
    def make_sound(self):
        return "Woof!"

    def move(self):
        return "Driving"


dog_car = DogCar()
print(dog_car.make_sound())
print(dog_car.move())


class A:
    name = "Ram"


class B:
    roll_number = "rollnumber of ram"


class C:
    course = "course of Ram"


class D(A, B, C):
    pass


obj = D()
print(obj.name)
print(obj.roll_number)
print(obj.course)
