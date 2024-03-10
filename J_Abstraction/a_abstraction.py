from abc import ABC, abstractclassmethod


class Vehical(ABC):
    @abstractclassmethod
    def drive(self):
        pass


class Car(Vehical):
    def drive(self):
        return "Car is Driving"


# Creating object of the class car
car = Car()
print(car.drive())
