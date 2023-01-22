# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР6 ЗАДАЧА1
###############################################################################
# Все задачи решать с помощью использования лямбд, filter, map, zip, enumerate, 
# List Comprehension 
# 1) Вводится список целых чисел в одну строчку через пробел. Необходимо 
# оставить в нем только двузначные числа. Реализовать программу с использованием 
# функции filter. Результат отобразить на экране в виде последовательности 
# оставшихся чисел в одну строчку через пробел.
# [1,2,3,4,22,234,24] ----> [22, 24]
###############################################################################

values = list(map(int, input(
    'Введите список целых чисел в одну строчку через пробел: ').split(' ')))
print('Исходный список чисел: ', values)
print('Список двузначных чисел: ', list(
    filter(lambda i: i // 10 and not i // 100, values)))

###############################################################################