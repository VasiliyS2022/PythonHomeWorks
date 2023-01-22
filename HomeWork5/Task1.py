# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР5 ЗАДАЧА1
##########################################################################################################
# Создайте программу для игры с конфетами человек против бота. Условие задачи: На столе лежит 120 конфета. 
# Играют два игрока делая ход друг после друга. Первый ход делает человек. За один ход можно забрать не 
# более чем 28 конфет. Победитель - тот, кто оставил на столе 0 конфет.
# 120 21 ---> 99 бот 4 -> 95 .... бот --->29 --> 27 >> 2конф
# a) Добавьте игру против бота
# Доп b) Подумайте как наделить бота ""интеллектом"" (Теория игр)
##########################################################################################################


import random
countCandy = 120


def MoveHuman(count):
    if count >= 28:
        maxMove = 28
    else:
        maxMove = count
    move = int(input(f'Вы можете взять не более {maxMove} конфет: '))
    
    if 0 < move <= maxMove:
        count -= move
        print(f'На столе осталось {count} конфет')
    else:
        print('Попробуйте еще раз!')
        count = MoveHuman(count)

    return count


def MoveComputerEasy(count):
    if count >= 28:
        move = random.randint(1, 28)
    elif 0 < count < 28:
        move = random.randint(1, count)
    print(f'Компьютер берет {move} конфет')
    count -= move
    print(f'На столе осталось {count} конфет')

    return count


def MoveComputerMiddle(count):
    if count > 116:
        move = count - 116
    elif count == 116 or count == 87 or count == 58 or count == 29:
        move = random.randint(1, 28)
    elif 87 < count <= 115:
        move = count - 87
    elif 58 < count <= 86:
        move = count - 58    
    elif 29 < count <= 57:
        move = count - 29
    elif 0 < count <= 28:
        move = count
    print(f'Компьютер берет {move} конфет')
    count -= move
    print(f'На столе осталось {count} конфет')

    return count


def CheckCount(count, temp):
    res = False

    if count == 0:
        print(f'Победил {temp}!')
        print('Игра окончена!')
        res = True

    return res


def SelectConfiguration(gr, wy):
    if gr == 0:
        gr = MoveComputerEasy
    elif gr == 1:
        gr = MoveComputerMiddle

    if wy == 0:
        s1 = MoveHuman
        s2 = gr
        name1 = 'Человек'
        name2 = 'Компьютер'
    elif wy == 1:
        s1 = gr
        s2 = MoveHuman
        name1 = 'Компьютер'
        name2 = 'Человек'
    
    return s1, s2, name1, name2

try:
    print('Выбор соперника: простой - 0, обученный компьютер - 1')
    selectGamer = int(input('Сделайте выбор (нажмите 0 или 1): '))
    print('Выбор первого хода: Ваш - 0', 'соперник - 1')
    selectWay = int(input('Сделайте выбор (нажмите 0 или 1): '))
    select = SelectConfiguration(selectGamer, selectWay)
    a = select[0](countCandy)
    b = select[1](a)
    while b > 0:
        a = select[0](b)
        temp = select[2]
        result = CheckCount(a, temp)
        if result == True:
            break
        if a > 0:
            b = select[1](a)
            temp = select[3]
            CheckCount(b, temp)
            if result == True:
                break
        else:
            break
except:
    ValueError: print('Попробуйте еще раз!')

##########################################################################################################