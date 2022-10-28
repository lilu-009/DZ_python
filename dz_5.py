# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 201 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) * Подумайте как наделить бота 'интеллектом'

# Человек против человека.

# from random import randint

# player_1 = input('Первый игрок, введите свое имя: ')
# player_2 = input('Второй игрок, введите свое имя: ')

# candy = 201
# print(f'На столе лежит {candy} конфет. Вам по очереди необходимо брать конфеты со стола. За один ход можно забрать не более 28 конфет. Выигрывает игрок, сделавший последний ход.')

# flag = randint(0,2)
# if flag:
#     print(f'{player_1}, первый ход ваш.')
# else:
#     print(f'{player_2}, первый ход ваш.')

# while candy > 28:
    
#     if flag:
#         var_1 = int(input(f'{player_1}, введите количество конфет, которое возьмете со стола: '))
#         while var_1 < 1 or var_1 > 28:
#             var_1 = int(input(f'{player_1}, введите количество конфет от 1 до 28: '))
#         candy = candy - var_1
#         flag = False
#         print(f'На столе осталось {candy} конфет.')
    
#     else:
#         var_2 = int(input(f'{player_2}, введите количество конфет, которое возьмете со стола: '))
#         while var_2 < 1 or var_2 > 28:
#             var_2 = int(input(f'{player_2}, введите количество конфет от 1 до 28: '))
#         candy = candy - var_2
#         flag = True
#         print(f'На столе осталось {candy} конфет.')

# if flag:
#     print(f'{player_1}, вы выиграли! Вам достаются все конфеты!')
# else:
#     print(f'{player_2}, вы выиграли! Вам достаются все конфеты!')



# Человек против бота.

# from random import randint

# player_1 = input('Первый игрок, введите свое имя: ')
# player_2 = 'БОТ'

# candy = 201
# print(f'На столе лежит {candy} конфет. Вам по очереди необходимо брать конфеты со стола. За один ход можно забрать не более 28 конфет. Выигрывает игрок, сделавший последний ход.')

# flag = randint(0,2)
# if flag:
#     print(f'{player_1}, первый ход ваш.')
# else:
#     print(f'{player_2}, первый ход ваш.')

# while candy > 28:
    
#     if flag:
#         var_1 = int(input(f'{player_1}, введите количество конфет, которое возьмете со стола: '))
#         while var_1 < 1 or var_1 > 28:
#             var_1 = int(input(f'{player_1}, введите количество конфет от 1 до 28: '))
#         candy = candy - var_1
#         flag = False
#         print(f'На столе осталось {candy} конфет.')
    
#     else:
#         var_2 = randint(1, 29)
#         print(f'{player_2} взял {var_2} конфет.')
#         candy = candy - var_2
#         flag = True
#         print(f'На столе осталось {candy} конфет.')

# if flag:
#     print(f'{player_1}, вы выиграли! Вам достаются все конфеты!')
# else:
#     print(f'{player_2} выйграл! Ему достаются все конфеты!')



# Создайте программу для игры в "Крестики-нолики".

# print('Игра "Крестики-нолики"')

# player_1 = input('Первый игрок, введите свое имя: ')
# player_2 = input('Второй игрок, введите свое имя: ')

# board = list(range(1,10)) # создали игровое поле

# def print_board(board): # вывели игровое поле
#     print('-' * 13)
#     for i in range(3):
#         print('|', board[0+i*3], '|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-' * 13)

# def take_input(player_name, player_token): # дали игрокам возможность "ставить" X или 0 в указанную клетку, если она свободна
#     valid = False
#     while not valid:
#         player_answer = int(input(f'{player_name}, введите номер клетки от 1 до 9, в которую желаете поставить {player_token}: '))
#         if 1 <= player_answer <= 9: 
#             if str(board[player_answer-1]) not in 'X0':
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print('Эта клетка уже занята!')
#         else:
#             print('Такой клетки нет!')

# def check_win(board): # проверяем игровое поле
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         print_board(board)
#         if counter % 2 == 0:
#             take_input(player_1, 'X')
#         else:
#             take_input(player_2, '0')
#         counter += 1
#         if counter > 4:
#             var = check_win(board)
#             if var:
#                 print ('Вы выиграли!')
#                 win = True
#                 break
#         if counter == 9:
#             print ('Ничья!')
#             break
#     print_board(board)

# main(board)



# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def rle_encode(data):
    
    encode = ''
    count = 1

    for i in range(len(data)):
        if i + 1 < len(data) and data[i] == data[i + 1]:
            count += 1
        else:
            encode += str(count) + data[i]
            count = 1
            
    return encode

file_2 = open('file_2.txt', 'r', encoding='utf_8')
data = file_2.read()
file_2.close()
file_3 = open('file_3.txt', 'w', encoding='utf_8')
file_3.write(rle_encode(data))

def rle_decode(data):

    count = ''
    decode = ''
    
    for i in range(len(data)):
        if not data[i].isalpha():
            count += data[i]
        else:
            decode = decode + data[i] * int(count)
            count = ''
    
    return decode

text = rle_decode(rle_encode(data))

file_4 = open('file_4.txt', 'w', encoding='utf_8')
file_4.write(text)
file_4.close()