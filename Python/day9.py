class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

car1 = Car("Ford", "Mustang", 1964)
print(car1.brand, car1.model, car1.year)

car2 = Car("Honda", "Civic", 2020)
print(car2.brand, car2.model, car2.year)

class Dog:
    def asignName(self, name):
        self.name = name

dog1 = Dog()
dog1.asignName("Rex")
print(dog1.name)

dog2 = Dog()
dog2.asignName("Max")
print(dog2.name)

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display(self):
        print(self.brand, self.model, self.year)

car3 = Car("Honda", "Civic", 2020)
car3.display()

