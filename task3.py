print('#1')
# number = int(input('Enter number   '))
value, number = 1, 400

while number > value ** 2:
    print(value ** 2, end='   ')
    value += 1
print('\n')

print('#2')
number = 54243
num = number
while number >= 10:
    number //= 10
    # print(number)
print(f'Первой цифрой числа {num} будет -> {number}')
print('\n')

print('#3')
number = 1224466889
num = number
min_digit = 9
while number > 0:
    if number % 10 < min_digit:
        min_digit = number % 10
        # print(min_digit)
    number //= 10
print(f'Минимальный числом {num} будет -> {min_digit}')
print('\n')

print('#4')
stroka = 'I want to tell you'
print(stroka[2], stroka[-2], stroka[:5], stroka[:-2], stroka[::2], stroka[1::2], stroka[::-1], stroka[::-2],
      len(stroka), sep='\n')

print('\n')

print('#5')  # либо через стрип, и из списка достать их в нужном порядке
stroka = 'Hello Egor'
space = stroka.find(' ')
print(stroka[space + 1:] + ' ' + stroka[:space])
print('\n')

print('#6')
stroka = 'level'
if stroka == stroka[::-1]:
    print('Это палиндром')
else:
    print('Слово не является палиндромом ')
print('\n')

print('#7')

stroka = 'это моя f строка, строки f очень удобны в python, чтобы ей воспользоваться, достаточно в начале текста перед ковычками поставить f'
find_f = stroka.find('f')
quantity_f = stroka.count('f')
if quantity_f == 1:
    print(f'В строке одно вхождение буквы "f" под индексом {find_f}')
elif quantity_f > 1:
    print(f'В строке вхождений буквы "f" {quantity_f} первое вхождение под индексом {find_f}')
else:
    print(f'В строке нет буквы "f"')
print('\n')

print('#8')
list1 = [1, 2, 3, 4, 5]
list2 = [1, 4, 5, 6]
minimum = 9
for i in range(len(list1)):
    if list1[i] not in list2 and list1[i] < minimum:
        minimum = list1[i]
for i in range(len(list2)):
    if list2[i] not in list1 and list2[i] < minimum:
        minimum = list2[i]
print(minimum)
print('\n')

print('#9')
count = 0
listt = [1, 2, 1, 4, 1, 6, 1, 7, 8, 1, 2, 4, 5]
for i in range(0, len(listt) - 1):
    if listt[i] < listt[i + 1]:
        count += 1
print(count)
print('\n\n')

print('#10')
stroka = 'Ха-ха-ха-ха'
letter_list = []
for i in stroka:
    if i not in letter_list:
        letter_list.append(i)
        print(i, end='')

print('\n\n')

print('#11')  # это на случай, если нет дробных чисел, и числа не написаны через пробел
text = ('В 2025 году планируется увеличение численности населения города до 1250000 человек, '
        'тогда как в 2020 году этот показатель составлял 1100000. Ожидается, что средний '
        'рост составит около 3.5% в год.')
alphabet_spec_symbols = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                         'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я',
                         'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т',
                         'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я',
                         '+', '-', '*', '/', '=', '!', '@', '#', '$', '%', '^', '&', '(', ')', '[', ']', '{', '}', '<',
                         '>', '?', ':', ';', ',', '.', '_', '|', '~']
for i in alphabet_spec_symbols:
    if i in text:
        text = text.replace(i, '')
text = text.split()
text = list(map(int, text))
print(max(text), '\n')

print('#11.1 поиск максимальной цифры')
text = ('В 2025 году планируется увеличение численности населения города до 1 250 000 человек, '
        'тогда как в 2020 году этот показатель составлял 1 100 000. Ожидается, что средний '
        'рост составит около 3,5% в год.')
digit_list = []
for i in text:
    if i.isdigit():
        digit_list.append(int(i))
print(max(digit_list))
print('\n\n')

print('#12')
letter_list = []
stroka = 'Тишина ночного города была нарушена лишь шорохом листьев под ногами.'
for i in stroka:
    if i not in letter_list:
        letter_list.append(i)
        print(i, end='')

print('\n\n')

print('#13')

print('\n\n')
