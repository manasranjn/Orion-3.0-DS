class Animal:
    def speak(self):
        print("Animal makes some sound")

class Cat(Animal):
    def run(slef):
        print("Cat is running")

    def speak(self):
        print("Meow")

cat1 = Cat()
# cat1.speak()
# cat1.run()

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print("Bhaw")

# dog1 = Dog()
# dog1.speak()


# Error
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
# print("Multiplication: ",a/b)

# Exception Handling
# a = int(input("Enter a number: "))
# b = int(input("Enter another number: "))
#
# try:
#     print("Division: ",a/b)
# except:
#     print("You cannot divide by zero")
# finally:
#     print("Always executes")

# try:
#     a = int("Hello")
# except ValueError:
#     print("Invalid input")
# except TypeError:
#     print("Invalid type")
# except Exception:
#     print("Something went wrong")


try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    try:
        result = x/y
        print("Division: ",result)
    except ZeroDivisionError as x:
        print(x)
except ValueError as e:
    print(e)
except TypeError as t:
    print(t)
