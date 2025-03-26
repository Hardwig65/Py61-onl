# 1
# class Math:
#     def __init__(self, num, num2):
#         self.num = num
#         self.num2 = num2
#
#     def Display(self):
#         print(f'Число 1 = {self.num}, Число 2 = {self.num2}')
#
#     def Numbers_sum(self):
#         print(f'Numbers_sum = {self.num + self.num2}')
#
#     def Numbers_max(self):
#         print(f'Numbers_max = {max(self.num, self.num2)}')
#
#     def Numbers_update(self, new_num, new_num2):
#         self.num = new_num
#         self.num2 = new_num2
#
#
# numbers = Math(10, 20)
#
# numbers.Display()
# numbers.Numbers_sum()
# numbers.Numbers_max()
# numbers.Numbers_update(100, 200)
# numbers.Display()
# 2
# class Counter:
#     def __init__(self, Counter_range, start_number=0):
#         self.start_number = start_number
#         self.Counter_range = Counter_range
#
#     def increase(self):
#         if self.start_number < self.Counter_range:
#             self.start_number += 1
#             print("Counter increased by 1")
#
#     def decrease(self):
#         if self.start_number > 0:
#             self.start_number -= 1
#             print("Counter decreased by 1")
#
#     def Counter_position(self):
#         print(f"Counter position = {self.start_number}")
#
#
# number = Counter(10)
# number.increase()
# number.Counter_position()
# number.decrease()
# number.Counter_position()
# 3
# class Shop:
#     def __init__(self, shelves: list):  # принимает начальный список продуктов
#         self.shelves = shelves
#
#     def add_product(self, product: str):
#         if product.title() not in self.shelves:
#             self.shelves.append(product.title())
#             print(f'Product {product} added at shelves')
#         else:
#             print("This product already exists")
#
#     def remove_product(self, product: str):
#         if product in self.shelves:
#             self.shelves.remove(product)
#         else:
#             print("No such product on shelves")
#
#     def show_shelves(self):
#         print(self.shelves)
#
#     def product_find(self, name: str):
#         for i in self.shelves:
#             if name.lower() in i.lower():
#                 print(f'Product {i} found')
#                 return
#         else:
#             print("No such product on shelves")
#
#
# Market = Shop(['Банан', 'Груша', 'Яблоки'])
# Market.add_product('бАнан')
#
# Market.product_find('бан')
#
# Market.show_shelves()
# 4
# class MoneyBox:
#
#     def __init__(self, capacity, monets=0):
#         self.capacity = capacity
#         self.monets = monets
#
#     def can_add(self, v):
#         if 0 <= self.monets + v <= self.capacity:
#             return True
#         else:
#             return False
#
#     def add(self, v):
#         if self.can_add(v):
#             self.monets += v
#             print('monets added')
#         else:
#             print('not enough capacity')
#
#     def display(self):
#         print(f'your monets = {self.monets}')
#
#     def can_add_check(self, v):
#         if self.can_add(v):
#             print(f'You can add {v} monets')
#         else:
#             print(f'Not enough capacity for {v} monets')
#
#
# m = MoneyBox(10)
# m.display()
# m.add(5)
# m.display()
# m.add(5)
# m.display()
# m.can_add_check(1)
