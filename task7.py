from datetime import datetime
import json

# print('#1')
# file = open('input.txt', 'w')
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# for i in numbers:
#     file.write(str(i) + '\n')
# print('\n')

# print('#2')
# file = open('input.txt', 'r')
# peremnogenie_chisel = 1
# for i in file:
#     peremnogenie_chisel *= int(i)
# file.close()
#
# file_output = open('output.txt', 'w')
# file_output.write(str(peremnogenie_chisel))
# file_output.close()
# print('\n')

# print('#3')
#
# today = datetime.today().date()
# with open('some_file.txt', 'r') as f:
#     for i in f:
#         line = i.split()
#
#         if int(line[1]) * int(line[2]) >= 1_000_000 and (
#                 today - datetime.strptime(line[-1], '%d.%m.%Y').date()).days >= 30:
#             print(f'{line[0]} хранится в складе больше 30 дней, и стоит {int(line[1]) * int(line[2])}')
#
# print('#4')
# counter_ballow = 0
# with open('Wiktorina', 'r') as questions, open('Answers', 'r') as answers:
#     for question in questions:
#         print(f'Ваш вопрос ----> {question.rstrip()}')
#
#         Your_answer = input('Введите свой ответ на вопрос, если он совпадает, вы получите балл ---> ')
#         Answer = answers.readline().strip()
#         if Your_answer.lower() == Answer.lower():
#             counter_ballow += 1
#             print('Вы получили одни балл!!!!, Продолжайте в том же духе')
#
# print(f'Ваше количество баллов по завершении {counter_ballow}')

print('#5')
my_dict = {10000: ('Egor', 12),
           10001: ('Masha', 21),
           10002: ('Kirill', 32),
           10003: ('Denis', 43),
           10004: ('Daniel', 55)}
with open('my_dict.json', 'w') as json_dict:
    json.dump(my_dict, json_dict)
