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
# text = ("apple orange banana umbrella elephant tree igloo cloud avocado pear")
# pattern = r"\b[aeoiu]\w+\b"
# print(re.findall(pattern=pattern, string=text))
# 5
# text = "Температура сегодня -5 градусов, вчера была +3, а завтра ожидается -12 или 0 по прогнозу. Также возможны колебания до +15 и -20."
# pattern = r"[+-]\d+"
# print(re.findall(pattern=pattern, string=text))
# 6
# texts = [
#     "The human mind is powerful.",
#     "A human can adapt quickly.",
#     "Many human inventions changed the world.",
#     "Human human human"
# ]
# repl = 'computer'
# pattern = 'human'
# for text in texts:
#     print(re.sub(pattern=pattern, repl=repl, string=text))
# # 7
# text = "Сегодня особенный день — 13-07-2025, запомни его."
# pattern = r"\b\d\d-\d\d-\d{4}\b"
# match = re.search(pattern, text)
# print(match.group())
# 8
# text = "Bob bought a blue bike before breakfast but forgot basket."
# pattern = r"\b\w{0,}b\w{0,}\b"
# print(re.findall(pattern, text, re.IGNORECASE))
# 9
# texts = [
#     "Heeellooo wooorld!!!",  # Повторы букв 'e', 'o', 'l' и '!'
#     "Sooo maaaany leeeetters...",  # Много одинаковых подряд идущих букв
#     "I looooveee Pythooon!",  # Повторы в "loveee" и "Pythooon"
#     "Whaaaat??? Nooooo waaaaay!!!",  # Повторы 'a', 'o'
#     "Noooo duplicates heeere...",  # Повторы в "Noooo", "heeere"
#     "Yessss, I’m sureeeee.",  # Повторы в "Yessss" и "sureeeee"
#     "Aaaarrrghhhh!!",  # Повторы 'a', 'r', 'g', 'h'
#     "Coooool beaaans!",  # Повторы 'o', 'a'
#     "Uuuuuh ohhhh...",  # Повторы 'u', 'h'
#     "Missssisssssippiiii"  # Повторы в "Missssisssssippiiii"
# ]
# pattern = r'(\w)\1+'
# repl = r"\1"
# for text in texts:
#     print(re.sub(pattern=pattern, string=text, repl=repl))
