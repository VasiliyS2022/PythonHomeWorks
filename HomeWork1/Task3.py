# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР1 ЗАДАЧА3
##########################################################################################################

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

def QuartNum(a, b):
    if (a > 0 and b > 0): return 1
    elif (a < 0 and b > 0): return 2
    elif (a < 0 and b < 0): return 3
    elif (a > 0 and b < 0): return 4
    else: return 0

numA = float(input('Введите значение A, не равное 0: '))
numB = float(input('Введите значение B, не равное 0: '))

quart = QuartNum(numA, numB)
print(f'Номер четверти точки A={numA} и точки B={numB} равен {quart}')

##########################################################################################################
