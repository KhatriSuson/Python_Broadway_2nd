class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


cat = Cat()
dog = Dog()

for i in (cat, dog):
    print(i.speak())
