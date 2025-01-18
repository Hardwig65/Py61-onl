print('#1')
print(17 / 2 * 3 + 2,
      2 + 17 / 2 * 3,
      19 % 4 + 15 / 2 * 3,
      15 + 6 - 10 * 4,
      17 / 2 % 2 * 3 ** 3,
      sep='\n', end='\n\n\n')

print('#2')
print(17 / 2 * (3 + 2),
      (2 + 17) / 2 * 3,
      19 % (4 + 15) / 2 * 3,
      (15 + 6 - 10) * 4,
      17 / 2 % (2 * 3 ** 3),
      sep='\n', end='\n\n\n')

print('#3')
print(f'{11 - 1.5 * 3} рублей', end='\n\n\n')

print('#4')
Anna_apples = 2
Paul_apples = 5
print(f'У Анны {Anna_apples} яблока')
print(f'У Пола {Paul_apples} яблок')
print(end='\n\n')

print('#5')
days = 5
print(f"{days} суток = {days * 24} часов = {days * 24 * 60} минут = {days * 24 * 60 * 60} секунд")
print(end='\n\n')

print('#6')
DaysGone = 182
print(f'Недель прошло {DaysGone // 7}, дней {DaysGone % 7}')
print(end='\n\n')

print('#7')
side_1, side_2 = 150, 65
print(f'Можно отрезать {(side_2 * side_1) // (30 * 30)}')
print(end='\n\n')

print('#8')

seconds = 4000
print(
    f'Прошел {seconds // 3600} час(ов), {(seconds - (seconds // 3600) * 3600) // 60} минут, {(seconds - (seconds // 3600) * 3600) % 60} секунд')
print(end='\n\n')

print('#9')  # для любого числа от 0-999
cash = 361

print(f'{cash // 100} купюр по 100 рублей')
print(f'{(cash - cash // 100 * 100) // 50} купюр по 50 рублей')
print(f'{((cash - cash // 100 * 100) - 50 * ((cash - cash // 100 * 100) // 50)) // 10} купюр по 10 рублей')
print(f'{((cash - cash // 100 * 100) - 50 * ((cash - cash // 100 * 100) // 50)) % 10} купюр по 1 рублю')
print(end='\n\n')

print('#10')
height = 5
up = 3
down = 2
count = 0
print(f'результат за первый день {height - up + down} метра')
height = height - up + down
print(f'результат за второй день {height - up + down} метра')
height = height - up + down
print(f'результат за третий день {height - up} метра')
print(f'Улитка прошла за {count} дней')
print(end='\n\n')

print('#11')
road_length = 56  # km
speed = 15  # km/h
hours = 3
minutes = 15
print(f'Пройденное байкером расстояние {road_length - (road_length - speed * (hours + speed / 60))}')
