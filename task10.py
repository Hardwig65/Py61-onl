# class RangeSquared:
#     def __init__(self, start: int = 0, end: int = 15):
#         self.start = start
#         self.end = end
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.start < self.end:
#             self.start += 1
#             return self.start ** 2
#         else:
#             raise StopIteration
#
#
# primer = RangeSquared()
#
# for i in primer:
#     print(i, end='   ')

# 2
# def factorial_gen(n):
#     fact = 1
#     for i in range(0, n + 1):
#         if i > 0:
#             fact *= i
#         yield fact
#
#
# n = 9
# gen = factorial_gen(n)
# for i in gen:
#     print(i, end=' ')

# 3
# def read_file_lines(filename):
#     with open(filename, 'r') as file_for_reading:
#         for line in file_for_reading:
#             yield line.strip()
#
#
# Lines = read_file_lines("Answers")
#
# for line in Lines:
#     print(line)
# 4
# def calculate_complex_formula(a: float, b: float, c: float, d: float, e: float, f: float, g: float, h: float) -> float:
#     result = ((b * c if a > 0 else -d / e) +
#               (f * (g + h) if g < h else -(d - f) / g))
#     return result
# 5
# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def name_age(self):
#         return self.name, self.age
#
#
# def greet(name, age):
#     if age >= 18:
#         print(f"Привет, {name}! Добро пожаловать на сайт для взрослых.")
#     else:
#         print(f'Привет, {name}! Добро пожаловать на детский сайт.')
#
#
# User1 = User('Алекс', 25)
# User2 = User('Лиза', 12)
#
# greet(*User1.name_age())
# greet(*User2.name_age())
