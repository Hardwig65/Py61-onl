from random import randint

# 1
# class BankAccount:
#     def __init__(self, balance: float = 0):
#         self.__balance = balance
#         self.daily_limit = 5000
#         self.withdrawals_today = 0
#         self.max_withdrawals = 3
#
#     def deposit(self, amount: float):
#         self.__balance += amount
#         print(f"Your deposit {amount}")
#
#     def withdraw(self, amount: float):
#
#         if amount > self.daily_limit or self.withdrawals_today >= self.max_withdrawals:
#             return print('Bigger than limit')
#
#         if amount <= self.__balance:
#             self.__balance -= amount
#             self.withdrawals_today += 1
#             self.daily_limit -= amount
#             print(f"Your withdrawal {amount} successfully")
#         else:
#             print('You do not have enough money!')
#
#     def get_balance(self):
#         print(f"Your balance is {self.__balance}")
# 2

# class Animal():
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.hunger = 100
#
#     def make_sound(self):
#         print("Making sound")
#
#     def eat(self):
#         print(f"{self.name} eating")
#         self.hunger += 10
#
#
# class Lion(Animal):
#     def make_sound(self):
#         print("Lion making sound")
#         self.hunger -= (randint(1, 5))
#
#     def hunt(self):
#         print("Lion hunting")
#         self.hunger -= (randint(5, 15))
#
#
# class ELephant(Animal):
#     def make_sound(self):
#         print("Elephant making sound")
#         self.hunger -= (randint(1, 10))
#
#     def trumpet(self):
#         print("ELephant trumping")
#         self.hunger -= (randint(1, 5))
#
#
# class Penguin(Animal):
#     def make_sound(self):
#         print("Penguin making sound")
#         self.hunger -= (randint(1, 10))
#
#     def swim(self):
#         print("Penguin is swimming")
#         self.hunger -= (randint(5, 15))
#
#
# lion = Lion('Leo', 5)
# penguin = Penguin("Peggy", 10)
# elephant = ELephant("Elly", 7)
#
# Animals = [lion, penguin, elephant]
#
# for animal in Animals:
#     animal.make_sound()

# # 3
# class Temperature:
#     def __init__(self, temperature=50):
#         self._temperature = temperature
#
#     @property
#     def temperature(self):
#         return self._temperature
#
#     @temperature.setter
#     def temperature(self, Temp):
#         if Temp > -273.15:
#             self._temperature = Temp
#         else:
#             raise ValueError("temperature must be > -273.15")
#
#     @property
#     def temperature_fahrenheit(self):
#         return self.temperature * 1.8 + 32
#
#     @property
#     def temperature_kelvin(self):
#         return self.temperature + 273.15
#
#
# t = Temperature(200)
# print(t.temperature)
#
# print(t.temperature_fahrenheit)
#
# print(t.temperature_kelvin)
