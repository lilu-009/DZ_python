# Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при хранении данных используется принцип: одна строка — один пользователь. Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл users_hobby.txt.

# file_users = open('users.txt', 'r', encoding='utf_8')
# content_1 = file_users.read()
# users = content_1.splitlines()

# file_hobby = open('hobby.txt', 'r', encoding='utf_8')
# content_2 = file_hobby.read()
# hobby = content_2.splitlines()

# users_hobby = dict(zip(users, hobby))

# file_users_hobby = open('users_hobby.txt', 'w', encoding='utf_8')
# for key in users_hobby:
#     file_users_hobby.write(f'{key}: {users_hobby[key]}\n')

# file_users.close()
# file_hobby.close()
# file_users_hobby.close()



# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# N = int(input('Введите натуральное число N: '))

# list = []
# i = 2

# while i <= N:
#     if N % i == 0:
#         list.append(i)
#         N //= i
#         i = 2
#     else:
#         i += 1
# print(f'Простые множители числа N: {list}')



# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# numbers_1 = list(map(int, input('Введите последовательность числе через пробел: ').split()))
# numbers_2 = []

# for i in range(len(numbers_1)):
#     if numbers_1.count(numbers_1[i]) == 1:
#         numbers_2.append(numbers_1[i])

# print(f'Список неповторяющихся элементов: {numbers_2}')



#  Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0

from fileinput import close
from random import randrange

k = int(input('Введите значение степени K: '))

file_1 = open('file_1.txt', 'w')
file_1.write(f'{randrange(100)}x^{k} + {randrange(100)}x + {randrange(100)} = 0')
file_1.close()