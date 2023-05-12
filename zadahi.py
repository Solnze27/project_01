# Задача 1
# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

string_length =  len(my_favorite_songs)
print(string_length)

print(my_favorite_songs[0 : -1])
print(my_favorite_songs[1 : -2])

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний,
#  второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.



# Задача 2
# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
    ]

#  Мыслила так, вот что слепила- в чем ошибка?:
# r = (my_favorite_songs[0][1] + my_favorite_songs[1][1] + my_favorite_songs[2][1])
# i = 0

# for i in my_favorite_songs:
#     r = ranint (0, k-1)
    # k = len(my_favorite_songs[r])
#     a = my_favorite_songs[r]
#     i = i + a[0]

# print(a[0]) 

from random import sample
r =  sample(my_favorite_songs, 3)
print('Три песни звучат' , r)


# Задача 3
# Задача 1.3.

# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом
# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней
    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней
    # Введите номер месяца: 15
    # Такого месяца нет!

user_input = input("Введите, пожалуйста, номер месяца: ")
month = int(user_input)
print('Вы ввели', month)

if 0 < month < 13:
    if month in (1, 3, 5, 7, 8, 10, 12):
        print('в этом месяце', 31, 'день')
    elif month in (4, 6, 9, 11):
        print('в этом месяце', 30, 'дней')
    elif month == 2:
        print('в этом месяце', 28, 'дней')
else:
    print('Вы ввели некорректное число. Введите число от 1 до 12.')


    # Задача 4
# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}
# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.
store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [ {'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [ {'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]}
# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"
# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"

for name_titles in titles:
    code_titles = titles[name_titles]
    total_price = 0
    total_quantity = 0
    for quantity_price in store[code_titles]:
        total_price = total_price + quantity_price['quantity'] * quantity_price['price']
        total_quantity += quantity_price['quantity']
    print(name_titles, '-', total_quantity, 'шт, общей стоимостью', total_price, 'рублей.')


    # Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
    pass

def maximum(arr):
    pass

print( minimum([4,6,2,1,9,63,-134,566])             , -134)
print( minimum([-52, 56, 30, 29, -54, 0, -110])     , - 110)
print( minimum([42, 54, 65, 87, 0])                 , 0)
print( minimum([5])                                 , 5)

print( maximum([-52, 56, 30, 29, -54, 0, -110])     , 56)
print( maximum([4,6,2,1,9,63,-134,566])             , 566)
print( maximum([5])                                 , 5)
print( maximum([534,43,2,1,3,4,5,5,443,443,555,555]), 555)
print( maximum([9])                                 , 9)

# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of (month):
    if month in [1, 2, 3]:
        return '1 квартал'
    elif month in [4, 5, 6]:
        return '2 квартал'
    elif month in [7, 8, 9]:
         return '3 квартал'
    elif month in [10, 11, 12]:
         return '4 квартал'

month = int(input("Введите номер месяца: "))
print(quarter_of(month))

#  Задача 2.3


# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

def switch_it_up(number):
    pass






# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

def remove_exclamation_marks(s):
    pass


# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    pass


# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"

def remove_word_with_one_em(s):
    pass