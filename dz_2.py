# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Пример: 6782 -> 23 0,56 -> 11

# number = input('Введите вещественное число: ')
# sum = 0

# for digit in number:
#     if digit.isdigit():
#         sum += int(digit)

# print(f'Сумма цифр числа {number} = {sum}')



# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N. Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('Введите число N: '))
# mult = []
# var = 1

# for i in range(1, N + 1):
#     var *= i
#     mult.append(var)

# print(f'Набор произведений чисел от 1 до {N} {mult}')



# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму. Пример: Для n = 6: {1: 2, 2: 2,25, 3: 2,37, 4: 2,44, 5: 2,49, 6: 2,52}

# n = int(input('Введите количество чисел последовательности n: '))
# list = {}

# for i in range(1, n + 1):
#     list[i] = round((1 + 1 / i) ** i, 2)

# print(f'Для n = {n}: {list}')



# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на введенных пользователем позициях.

# N = int(input('Введите количество элементов N больше 1: '))

# if N > 1:
#     list = []
    
#     from random import randint
    
#     for i in range(1, N+1):
#         list.append(randint(-N, N))
#     print(list)

#     j = int(input('Введите первую позицию элемента - '))
#     k = int(input('Введите вторую позицию элемента - '))

#     if j < N and k < N:
#         print(f'Произведение элементов {list[j]} и {list[k]} = {list[j] * list[k]}')
#     else:
#         print('Таких позиций в списке нет')

# else:
#     print('Ошибка: количество элементов не больше 1')


# Реализуйте алгоритм перемешивания списка.

list = [1, 8, 45, 15, 38]
i = 0

while i < len(list) // 2:
    var = list[(len(list)-1)-i]
    list[(len(list)-1)-i] = list[i]
    list[i] = var
    i += 1

print(list)