# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР3 ЗАДАЧА3
##########################################################################################################

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным 
# значением дробной части элементов. Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

def CreateRandomList(l):
    lt = [round(random.uniform(1, 10), 2) for i in range(l)]

    return lt

def DifferenceFraction(l):
    maxValue, minValue = 0, 1

    for i in l:
        a = round(i - int(i), 2)
        if a > maxValue:
            maxValue = a
        if a < minValue:
            minValue = a

    return maxValue - minValue

lengthList = int(input("Задайте длину списка: "))
list = CreateRandomList(lengthList)
print(f'Разницa между максимальным и минимальным значением дробной части элементов списка {list}' + 
f' составляет {round(DifferenceFraction(list), 2)}')

##########################################################################################################