print('#1')


def minimum(number1: int, number2: int) -> int:
    return min(number2, number1)


print(minimum(2, 3))
print('\n\n')

print('#2')

print(minimum(minimum(5, 4), minimum(3, 6)))

print('\n\n')

print('#3')
x1, y1, x2, y2 = 1, 2, 3, 4


def distance(x1: int, y1: int, x2: int, y2: int) -> float:
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print(distance(x1, y1, x2, y2))
print('\n\n')

print('#4')
number = 7


def prostoe_chislo(a: int) -> None:
    for i in range(2, a):
        if number % i == 0:
            print('Число составное')
            break
    else:
        print('Число простое')


prostoe_chislo(number)
print('\n\n')

print('#5')
n = 8


def fibonacci(n: int) -> int:
    number2, number3 = 1, 1
    for i in range(0, n - 1):
        number2, number3 = number3, number2 + number3
    print(number2)


fibonacci(n)
print('\n\n')

print('#6')
number = 101


def closest_mod_5(n: int) -> int:
    result = (n // 5) * 5 if n % 5 == 0 else (n // 5) * 5 + 5
    return result


print(closest_mod_5(number))

print('\n\n')

print('#7')
spisok = [2, 12, 44, 32, 1313, 43, 11, 121, 22]


def modify_list(spisok: list) -> None:
    for i in range(len(spisok) - 1, -1, -1):
        if spisok[i] % 2 == 1:
            spisok.pop(i)
        else:
            spisok[i] = spisok[i] // 2
    print(spisok)


modify_list(spisok)
print('\n\n')

print('#8')

name = 'avdsabdfv123'


def name_check(name: str) -> bool:
    bad_symbols = '!@#$%^&*()+-'
    for i in name:
        if i in bad_symbols:
            return False
        elif name[0].isdigit():
            return False
        else:
            return True


while name.lower() != 'хватит':
    name = input('Введите имя! ')
    if name_check(name) is False:
        print('Нельзя использовать')
    else:
        print('Можно использовать')
    print('\n')
else:
    print('Работа закончена')
