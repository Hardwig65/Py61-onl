import time
import datetime

print('#1')
words = ["яблоко", "банан", "вишня", "груша", "персик", "ананас", "манго", "апельсин", "киви", "лимон"]
sorted_words = sorted(words, key=len, reverse=True)
print(sorted_words)
print()

print('#2')
sorted_by_a_words = sorted(words, key=lambda word: word.count('а'))
print(sorted_by_a_words)
print()

print('#3')
school = {'9a': 5,
          '9b': 6,
          '9c': 7,
          '9d': 8,
          '9e': 9}

school['9a'] = 11  # Изменение значения
school['9f'] = 12  # Добавление ключ:значение
del school['9b']  # удаление ключ:значение, так же методом school.pop('9b')
print(school)
print(f'Количество ученико во всех классах {sum(school.values())}')  # Вывод суммы значений

print('\n')

print('#4 задача закомментирована')

# phone_numbers = {}
# text = input('Введите строку -> ')
# while text != '.':
#     splitted_text = text.split()
#     if len(splitted_text) == 2:
#         phone_numbers[splitted_text[0]] = splitted_text[1]
#         print('Произошла запись/перезапись контакта ')
#     elif len(splitted_text) == 1 and splitted_text[0] in phone_numbers:
#         print(f'Номер контакта по имени -> {phone_numbers[splitted_text[0]]}')
#     else:
#         print('не найдено')
#     text = input('Введите строку -> ')

print('\n')

print('#5')


def get_element(lst: list, index: int):
    try:
        return lst[index]
    except IndexError as c:
        return 'IndexError "Ошибка: индекс вне диапазона"'


print(get_element([1, 2, 3, 4, 5], 5))

print('#6')


def retry_on_exception(func):
    def wrapper(value, retries):
        try:
            return (func(value, retries))
        except ValueError:
            print('Нельзя преобразовать слово в число')
            print()
            for i in range(retries):
                try:
                    return func(value, retries)
                except ValueError:
                    print('Нельзя преобразовать слово в число')

    return wrapper


@retry_on_exception
def retries(value: str, retries: int):
    value = int(value)
    return value


print(retries('12a', 3))


def time_limit_check(limit):
    def my_decorator(func):
        def wrapper():
            start = datetime.datetime.now()
            func()
            print(datetime.datetime.now() - start)
            if (datetime.datetime.now() - start).total_seconds() > limit:
                raise TimeoutError("Функция превысила лимит времени!")
            else:
                print('Задача справилась с лимитом времени')

        return wrapper

    return my_decorator


@time_limit_check(limit=1)
def long_func():
    for i in range(2000000):
        print('looooooong function')


long_func()
print('\n')

print('#7*')

str_from_book = 'a aa abC aa ac abc bcd a'.lower()
str_from_book = str_from_book.split()
unique_dict = {}

for i in range(len(str_from_book)):
    unique_dict[str_from_book[i]] = str_from_book.count(str_from_book[i])

for i in unique_dict:
    print(i, unique_dict[i])
