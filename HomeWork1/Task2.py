# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР1 ЗАДАЧА2
##########################################################################################################

# (!!!Доп!!!) Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех 
# значений предикат.

def Meaning(x, y, z):
        if x == '1': x = True
        elif x == '0': x = False
        if y == '1': y = True
        elif y == '0': y = False
        if z == '1': z = True
        elif z == '0': z = False

        if ((not(x or y or z)) == ((not x) and (not y) and (not z))): flag = True
        else: flag = False
        return flag

numX = input('Введите значение X(0 или 1): ')
numY = input('Введите значение Y(0 или 1): ')
numZ = input('Введите значение Z(0 или 1): ')
if ((numX == '0' or numX == '1') and (numY == '0' or numY == '1') and (numZ == '0' or numZ == '1')):
    result = Meaning(numX, numY, numZ)
    print(result)
else: print("Введены ошибочные данные, попробуйте еще раз!")

##########################################################################################################
