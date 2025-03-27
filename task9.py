from random import randint

# class BankAccount:
#     def __init__(self, balance: float = 0):
#         self.__balance = balance
#         self.daily_limit = 5000
#         self.withdrawals_today = 0
#         self.max_withdrawals = 3
#         self.withdrawals_limit = 0
#
#     def deposit(self, amount: float):
#         self.__balance += amount
#         print(f'Deposit successful! Remaining balance: {self.__balance}')
#
#     def withdraw(self, amount: float):
#         if self.withdrawals_today <= self.max_withdrawals and amount <= self.__balance and amount + self.withdrawals_limit <= self.daily_limit:
#             self.withdrawals_today += 1
#             self.__balance -= amount
#             self.withdrawals_limit += amount
#             print(f'Withdrawal successful! Remaining balance: {self.__balance}')
#         else:
#             print('You reached the daily limit or withdrawal amount is too high')
#
#     def get_balance(self):
#         print(f'Balance: {self.__balance}')
#
#     def get_info(self):
#         print(f'Daily limit: {self.daily_limit}')
#         print(f'Withdrawals today: {self.withdrawals_today}')
#         print(f'Max withdrawals: {self.max_withdrawals}')
#
#
# Egor = BankAccount(1000)
#
# Egor.get_balance()
# Egor.withdraw(1000)
# Egor.deposit(10000)
#
#
# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.hunger = 100
#         print(f"animal {self.name} added")
#
#     def Hunger_state(self):
#         print(f"{self.name} hunger state is {self.hunger}")
#
#     def make_sound(self):
#         self.hunger -= randint(1, 5)
#         print(f"{self.name} making sound")
#
#
#     def eat(self):
#         self.hunger = 100
#
#
# class Lion(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def hunt(self):
#         self.hunger -= randint(10, 20)
#         print(f"Lion hunt, The hunger remains {self.hunger}")
#
#
# class Elephant(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def trumpet(self):
#         self.hunger -= randint(10, 20)
#         print(f"Elephant Trumpet, The hunger remains {self.hunger} ")
#
#
# class Penguin(Animal):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#
#     def swim(self):
#         self.hunger -= randint(10, 20)
#         print(f"Penguin swim, The hunger remains {self.hunger} ")
#
#
# Peggy = Penguin("Peggyino", 3)
# Simba = Lion("Simbino", 5)
# Elelfan = Elephant("Elelfino", 7)
#
# print()
#
# Animals = [Peggy, Simba, Elelfan]
# for animal in Animals:
#     animal.make_sound()
#     animal.Hunger_state()
#     print()
# class Temperature:
#     def __init__(self, temperature=0):
#         self.__temperature = temperature
#         print("temp setted")
#
#     @property
#     def temp(self):
#         return self.__temperature
#
#     @temp.setter
#     def temp(self, new_temperature):
#         if new_temperature > -273.15:
#             self.__temperature = new_temperature
#             print('Temperature changed to {}'.format(new_temperature))
#         else:
#             print('Nothing changed, Temperature is too low')
#
#     def cels_to_farenh(self):
#         return self.temp * 1.8 + 32
#
#     def cels_to_kelvin(self):
#         return self.temp - 273.15
#
#
# T = Temperature(19)
# print(T.temp)
# T.temp = 100
# print(T.temp)
# print(T.cels_to_kelvin())
#
