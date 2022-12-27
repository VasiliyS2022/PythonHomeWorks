# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР3 ЗАДАЧА2
##########################################################################################################

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и 
# предпоследний и т.д. Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

def CreateRandomList(l):
    lt = [random.randint(-10, 10) for i in range(l)]

    return lt

def MultiplicationCoupleValue(l):
    resList = []

    for i in range((len(l) + 1) // 2):
        resList.append(l[i] * l[-i - 1])

    return resList

lengthList = int(input("Задайте длину списка: "))
list = CreateRandomList(lengthList)
print(f'Произведение пар чисел списка {list} выглядит так: {MultiplicationCoupleValue(list)}')

##########################################################################################################