# # 1
# class Mathematics:
#     def __init__(self, number_1=2, number_2=3):
#         self.number_1 = number_1
#         self.number_2 = number_2
#
#     def monitor(self):
#         print(f"Число один будет:{self.number_1} \n"
#               f"Числом два будет:{self.number_2}")
#
#     def number_change(self, new_number1, new_number2):
#         self.number_1 = new_number1
#         self.number_2 = new_number2
#         print('numbers changed')
#         self.monitor()
#
#     def math_sum(self):
#         return self.number_1 + self.number_2
#
#     def math_max(self):
#         return max(self.number_1, self.number_2)
#

# 2
# class Counter:
#     def __init__(self, counter_start=0, counter_end=10):
#         self.counter_start = counter_start
#         self.counter_end = counter_end
#
#     def counter_display(self):
#         print(f"counter in {self.counter_start}")
#
#     def counter_increment(self):
#         self.counter_start += 1
#         print("Incremented counter")
#
#     def counter_decrement(self):
#         self.counter_start -= 1
#         print("Decremented counter")
#
#
# counter = Counter()
# counter.counter_display()
# counter.counter_increment()
# counter.counter_increment()
# counter.counter_display()

# 3
# class Shop:
#     def __init__(self, Products_list=["Банан", 'Яблоко', "Груша"]):
#         self.Products_list = Products_list
#
#     def get_product_list(self):
#         return self.Products_list
#
#     def product_find(self, Product_name):
#         if Product_name.title() in self.Products_list:
#             print(f"Yes, we have {Product_name}")
#         else:
#             print(f"No, we don't have {Product_name}")
#             for Product in self.Products_list:
#                 if Product_name.lower() in Product.lower():
#                     print(f'maybe you meaning {Product}')
#
#     def product_add(self, Product):
#         self.Products_list.append(Product.title())
#
#     def product_remove(self, Product):
#         self.Products_list.remove(Product.title())
#
#
# s = Shop()
#
# s.product_find('анан')
# s.product_add("аРБУЗ")
# print(s.get_product_list())
# s.product_remove('АРБУЗ')
# print(s.get_product_list())
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self._current_coins = 0

    def can_add(self, v):
        if self.capacity >= v + self._current_coins:
            return True

    def Box_info(self):
        print(f'{self._current_coins} coins left')

    def add(self, v):
        if self.can_add(v):
            self._current_coins += v
            print(f'added {v}')
        else:
            print('Cannot add')


Box = MoneyBox(8)
Box.add(7)
Box.Box_info()
Box.add(7)
Box.Box_info()
