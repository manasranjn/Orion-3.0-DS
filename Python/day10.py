# class Employees:
#     def __init__(self, name, e_id, salary):
#         self.name = name
#         self.e_id = e_id
#         self.salary = salary
#
#     def login(self):
#         print(f"{self.name} has logged in")
#
#     def logout(self):
#         print(f"{self.name} has logged out")
#
#     def taskCompleted(self):
#         print(f"{self.name} has completed a task")
#
#     def show_salary(self):
#         print(f"{self.name}'s salary is {self.salary}")
#
#
# employee1 = Employees("Sumit", 1, 50000)
# employee1.login()
# employee1.taskCompleted()
# employee1.logout()
# employee1.show_salary()
#
# employee2 = Employees("Rohit", 2, 60000)
# employee2.login()
# employee2.taskCompleted()
# employee2.logout()
# employee2.show_salary()

# Constructor

# class Animal:
#     def __init__(self):
#         self.type = "Mammal"
#         print("Animal created")
#
# object1 = Animal()
# print(object1.type)
#
# object2 = Animal()
# print(object2.type)
# #
# class Animal:
#     def __init__(self, name):
#         self.name = name
#         print("Animal created")
#
# object1 = Animal("Dog")
# print(object1.name)
#
# object2 = Animal("Cat")
# print(object2.name)
#
# class Animal:
#     def __init__(slef, name="Dog"):
#         slef.name = name
#         print("Animal created")
#
#
# object1 = Animal()
# print(object1.name)
#
# object2 = Animal("Cat")
# print(object2.name)

# Polymorphism
# print(len("Hello"))
# print(len([1,2,3,4,5]))
# print(len({1,2,3,4,5}))

# class Dog:
#     def speak(self):
#         print("Woof")
#
# class Cat:
#     def speak(self):
#         print("Meow")
#
# dog1 = Dog()
# dog1.speak()
#
# cat1 = Cat()
# cat1.speak()

# Encapsulation

class Bank:
    def __init__(self, account , balance):
        self.__balance = balance
        self.account = account

    def desposit(self,amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")

    def withdraw(self,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance

account1 = Bank("123456", 1000)
print(account1.get_balance())
account1.desposit(100)
print(account1.get_balance())
account1.withdraw(500)
print(account1.get_balance())

# print(account1.balance)
print(account1.account)