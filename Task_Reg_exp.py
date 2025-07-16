import re

# 1 с re.I
# texts = [
#     "hello CAt",
#     "python 3.9",
#     "version2",
#     "no cats here",
#     "123abccat",
#     "cAaBtC"
#     'caat'
# ]
# pattern = r"cat"
# for text in texts:
#     if re.search(pattern=pattern, string=text, re.I):
#         print(text)

# 2
# texts = [
#     "hello zCAtz",
#     "python z3.9z",
#     "vzerzsion2",
#     "nzo czats here",
#     "123abccat",
#     "zcAaBtCz",
#     'caaztz'
# ]
# pattern = r"z...z"
# for text in texts:
#     if re.search(pattern=pattern, string=text):
#         print(text)
# 3
# numbers = [
#     "9876543210",  # ✅ начинается с 9, длина 10
#     "8765432109",  # ✅ начинается с 8, длина 10
#     "7894561230",  # ❌ начинается с 7
#     "912345678",  # ❌ только 9 цифр
#     "998877665544",  # ❌ слишком длинный
#     "8123456789",  # ✅ начинается с 8, длина 10
#     "9000000000",  # ✅ начинается с 9, длина 10
#     "88888",  # ❌ слишком короткий
#     "899a123456",  # ❌ содержит букву
#     "9123456789"  # ✅ начинается с 9, длина 10
# ]
# pattern = r"^(8|9)\d{9}$"
#
# for number in numbers:
#     if re.match(pattern=pattern, string=number):
#         print(number)
# 4
