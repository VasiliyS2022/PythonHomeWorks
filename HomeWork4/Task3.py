# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР4 ЗАДАЧА3
##########################################################################################################

# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.
# Ввод:
# 3 1 2 3
# Вывод:
# 2 1

def NonRepetitiveValues(lt):
    list1 = []

    for i in range(len(list)):
        count = 0
        for j in range(len(list)):
            if list[i] == list[j]:
                count += 1
                if count == 2:
                    list1.append(i)

    list1.reverse()
    for i in range(len(list1)):
        list.pop(list1[i])
    print(*list)

list = [i for i in input('Введите элементы через пробел: ').split()]
NonRepetitiveValues(list)

##########################################################################################################