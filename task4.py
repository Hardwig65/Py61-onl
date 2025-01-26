print('#1')


def minimum(a, b):
    return min(a, b)


print(minimum(2, 3))
print('\n\n')

print('#2')

print(minimum(minimum(5, 4), minimum(3, 6)))

print('\n\n')

print('#3')
x1, y1, x2, y2 = 1, 2, 3, 4


def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


print(distance(x1, y1, x2, y2))
print('\n\n')

print('#4')
number = 7


def prostoe_chislo(a):
    for i in range(2, a):
        if number % i == 0:
            print('Число составное')
            break
    else:
        print('Число простое')


prostoe_chislo(number)
print('\n\n')
