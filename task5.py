print('#1')
print([i for i in range(11, 100, 2)])
print('\n')

print('#2')
print([i ** 2 for i in range(1, 11)])
print('\n')

print('#3')
print([i for i in range(100, 1000) if i % 3 == 0 and i % 5 == 0])
print('\n')

print('#4')
# start, stop, stepen = map(int, input().split())
start, stop, stepen = 2, 10, 3
print([i ** stepen for i in range(start, stop)])
print('\n')

print('#5')
# digits = [int(input()) for i in range(10)]
digits = [23, 12, 302, 530, 3, 2, 100, 312]
digits = list(map(str, digits))  # сделал строки
new_digits = list(filter(lambda element: '0' in element, digits))
print(*list(map(int, new_digits)))  # вернул в int
print('\n')

print('#6')
words = ["apple", "banana", "cherry", "graape", "melon", "kiwi", "peach", "plum", "orange"]

print(list(filter(lambda words: words.count('a') >= 2, words)))
print('\n')

print('#7')
new_words = list(map(lambda words: words.upper(), words))
print(*new_words)

print('\n')

print('#8')

mixed_strings = ["a1b2c3", "xyz", "hello", "42life", "m4gic", "c0d3r", "abc789", "qwe", "xyz2024", "test99"]


def digit_delete(word: str) -> str:
    for i in word:
        if i.isdigit():
            word = word.replace(i, '')
    return word


digit_delete(mixed_strings[0])
print(list(map(digit_delete, mixed_strings)))

print('\n')

print('#9')
numbers = '4 8 0 3 4 2 0 3'
numbers_list = list(map(int, numbers.split()))
new_numbers_list = []
for i in numbers_list:
    if numbers_list.count(i) >= 2:
        new_numbers_list.append(i)
print(*set(new_numbers_list))
print('\n')

print('#10')


def prostoe_chislo(number: int) -> bool:
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


n = 100
print(*filter(prostoe_chislo, [i for i in range(1, n + 1)]))
print('\n')

print('#11')
spisok = list(map(int, '7 3 4 5'.split()))
i = 1
while i < len(spisok):
    spisok.insert(i, 0)
    i += 2
print(*spisok)
print('\n')

print('#12')
spisok = [10, 2]
new_spisok = []
index_smaller, index_bigger = -1, 1
for i in range(0, len(spisok)):
    if index_bigger < len(spisok):
        new_spisok.append(spisok[index_smaller] + spisok[index_bigger])
        index_smaller += 1
        index_bigger += 1
    else:
        index_bigger *= -1
        new_spisok.append(spisok[index_smaller] + spisok[index_bigger])
print(new_spisok)
print('\n')
