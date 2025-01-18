print('#1')
# num_1 = int(input('Введите число'))
num_1 = 103
if num_1 % 10 == 3:
    print(True)
else:
    print(False)
print(end="\n\n")

print('#2')
# number1, number2, number3 = map(int, input().split())
number1, number2, number3 = 1, 2, -1
if number1 >= 0 and number2 >= 0 and number3 >= 0:
    print(True)
else:
    print(False)
print(end="\n\n")

print('#3')
number1, number2 = 120, 4
if number1 % 2 == number2 % 2:
    print(f'Числа являются четными !{True}!')
else:
    print(f'Числа являются нечетными !{False}! ')
print(end="\n\n")

print('#4')
side_a, side_b, side_c = 1, 2, 1
if side_a == side_b == side_c:
    print('equilateral')
elif side_a == side_b or side_b == side_c or side_c == side_a:
    print('isosceles')
else:
    print('scalene')
print(end="\n\n")

print('#5')
count = 0
nums = [321, 124, 432]
for i in nums:
    if i % 2 == 0:
        count += 1
print(f'количество четных чисел {count}')
print(end="\n\n")

print('#6')
number = 63
if 0 <= number % 10 + number // 10 < 10:
    print(f'Сумма его цифр является однозначной {number % 10 + number // 10}')
else:
    print(f'Сумма его цифр является двузначной {number % 10 + number // 10}')
print(end="\n\n")

print('#7')
four_digit_number = str(1111)
if len(set(four_digit_number)) == 1:
    print('Все цифры одинаковы')
else:
    print('Есть разные цифры')
print(end="\n\n")

print('#8')
year = 2000
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print('Високосный')
else:
    print('Не високосный')
print(end="\n\n")

print('#9')
for i in range(20):
    print('10')
print(end="\n\n")

print('#10 stop !включительно!')
start, stop = 1, 9
for i in range(start, stop + 1):
    print(i)
print(end="\n\n")

print('#11 stop !включительно!')
start, stop = 100, -100
for i in range(start, stop - 1, -1):
    print(i, end=' ')
print(end="\n\n")

print('#12 stop !включительно!')
summa = 0
start, stop = 100, 500
for i in range(start, stop + 1):
    summa += i
print(summa)
print(end="\n\n")

print('#13 stop !включительно!')
proizvedenie = 1
start, stop = 5, 20
for i in range(start, stop + 1):
    proizvedenie *= i
print(proizvedenie)
print(end="\n\n")

print('#14')
factoriall = 1
for i in range(1, 6):
    factoriall *= i
print(factoriall)  # или из библиотеки math print(factorial(5))
print(end="\n\n")

print('#15')
# n = input('Введите натуральное число до 1000')
n = 214
for i in range(1, n + 1):
    if i % 10 == 1 and i not in [j for j in range(11, 1000, 100)]:
        print(f'На лугу {i} корова')
    elif ((i % 10 == 2 and i not in [j for j in range(12, 1000, 100)]) or
          (i % 10 == 3 and i not in [j for j in range(13, 1000, 100)]) or
          (i % 10 == 4 and i not in [j for j in range(14, 1000, 100)])):
        print(f'На лугу {i} коровы')
    else:
        print(f'На лугу {i} коров')
print(end="\n\n")

print('#16')
# n = input('Введите натуральное число')
n = 8
number2, number = 1, 1
for i in range(0, n):
    print(number2, end=' ')
    number2, number = number, number2 + number
print(end="\n\n")

print('#17')
x1, y1, x2, y2 = 1, 1, 2, 2
# a
if x1 + y1 % 2 == x2 + y2 % 2:
    print('Поля одного цвета')
else:
    print('Поля разных цветов')
# b

if ((x1 - y1 == x2 - y2) or
        (x1 + y1 == x2 + y2) or
        (x1 == x2 or y1 == y2)):
    print('Угрожает')
else:
    print('Не угрожает')
