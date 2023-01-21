# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР5 ЗАДАЧА3
##########################################################################################################
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные данные хранятся в отдельных текстовых файлах.
# stroka = "aaabbbbccbbb"
# ....
# stroka = "3a4b2c3b"
# Вывод: stroka = "aaabbbbccbbb"
##########################################################################################################


def FileReading():
    with open('TextTest.txt', 'r') as file:
        line = file.readline()

    return line


def CompressLine(line):
    temp = line + '!'
    list = []
    count = 1

    for i in range(len(temp) - 1):
        if temp[i] == temp[i + 1]:
            count += 1
        else:
            list.append(count)
            list.append(temp[i])
            count = 1
    
    return list


def RecoveryLine(list):
    newList = []

    for i in range(0, len(list) - 1, 2):
        a = list[i] * list[i + 1]
        newList.append(a)

    return newList


sourseString = FileReading()
print('Исходная строка:', sourseString, sep='\n')
compressString = CompressLine(sourseString)
recoveryString = RecoveryLine(compressString)
compressString = ''.join(map(str, compressString))
recoveryString = ''.join(map(str, recoveryString))
print('Сжатая строка:', compressString, sep='\n')
print('Восстановленная строка:', recoveryString, sep='\n')

##########################################################################################################