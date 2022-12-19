# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР1 ЗАДАЧА4
##########################################################################################################

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат 
# точек в этой четверти (x и y).

import random

def QuartNum(num):
    if num == '1': # a > 0 and b > 0
        a = random.randrange(1, 50)
        b = random.randrange(1, 50)
    elif num == '2': # a < 0 and b > 0
        a = random.randrange(-50, -1)
        b = random.randrange(1, 50)
    elif num == '3': # a < 0 and b < 0
        a = random.randrange(-50, -1)
        b = random.randrange(-50, -1)
    elif num == '4': # a > 0 and b < 0
        a = random.randrange(1, 50)
        b = random.randrange(-50, -1)
    else:
        a = 0
        b = 0
    return a, b

def Range(q):
    if q == '1': # a > 0 and b > 0
        d = 'a > 0 и b > 0'
    elif q == '2': # a < 0 and b > 0
        d = 'a < 0 и b > 0'
    elif q == '3': # a < 0 and b < 0
        d = 'a < 0 и b < 0'
    elif q == '4': # a > 0 and b < 0
        d = 'a > 0 и b < 0'
    else:
        d = 0
    return d

numQuart = input('Введите номер четверти от 1 до 4: ')

points = QuartNum(numQuart)
quart = Range(numQuart)

print(f'В четверти {numQuart} диапазон равен {quart}, значения точек A и B могут быть равны {points}')

##########################################################################################################