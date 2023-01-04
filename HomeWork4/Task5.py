# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР4 ЗАДАЧА5
##########################################################################################################

# *** 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, 
# содержащий сумму многочленов.
# 2*x^2 + 4*x      5*x^2 + 2*x
#          7x^2 + 6x
# 2*x^6 + 4*x      5*x^2 + 2*x
#     2*x^6 + 5*x^2 + 6*x

# Данное решение работает только с многочленами формата "Значение*x^Степень + Значение*x"

def ReadFiles():
    with open('5_1.txt', 'r') as file:
        line1 = file.readline()
    with open('5_2.txt', 'r') as file:
        line2 = file.readline()

    return line1, line2

def CalculationDegrees(line1, line2):
    m1 = []
    for i in line1:
        if i.isdigit():
            m1.append(int(i))

    m2 = []
    for i in line2:
        if i.isdigit():
            m2.append(int(i))

    return m1, m2

def Polinominal(m1, m2):
    if m1[1] == m2[1]:
        print(str(m1[0] + m2[0]) + '*x^' + str(m1[1]) + ' + ' + str(m1[2] + m2[2]) + '*x')
        res = str(m1[0] + m2[0]) + '*x^' + str(m1[1]) + ' + ' + str(m1[2] + m2[2]) + '*x'
    else:
        print(str(m1[0]) + '*x^' + str(m1[1]) + ' + ' + str(m2[0]) + '*x^' + str(m2[2]) + ' + ' + str(m1[2] + m2[2]) + '*x')
        res = str(m1[0]) + '*x^' + str(m1[1]) + ' + ' + str(m2[0]) + '*x^' + str(m2[2]) + ' + ' + str(m1[2] + m2[2]) + '*x'

    with open('5_3.txt', 'a') as file:
        file.writelines(res)

txt = ReadFiles()
res = CalculationDegrees(txt[0], txt[1])
Polinominal(res[0], res[1])

##########################################################################################################