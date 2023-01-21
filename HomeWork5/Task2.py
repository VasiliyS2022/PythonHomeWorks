# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР5 ЗАДАЧА2
##########################################################################################################
# Создайте программу для игры в ""Крестики-нолики"" человек vs человек.
##########################################################################################################


dict = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}


def Graphic(dict):
    print('-------------')
    print('|', dict[1], '|',  dict[2], '|',  dict[3], '|')
    print('-------------') 
    print('|', dict[4], '|', dict[5], '|', dict[6], '|')
    print('-------------') 
    print('|', dict[7], '|', dict[8], '|', dict[9], '|')
    print('-------------') 


def MoveFirstPlayer(d):
    cell = int(input('Ход первого игрока. Введите номер клетки для хода: '))
    if d[cell] != 'X' and d[cell] != 'O':
        d[cell] = 'X'
    else:
        print('Эта клетка уже занята')
        cell = MoveFirstPlayer(d)

    return dict


def MoveSecondPlayer(d):
    cell = int(input('Ход второго игрока. Введите номер клетки для хода: '))
    if d[cell] != 'X' and d[cell] != 'O':
        d[cell] = 'O'
    else:
        print('Эта клетка уже занята')
        cell = MoveSecondPlayer(d)

    return dict


def CheckingStatusX(d):
    v = 'X'
    if ((d[1] == v and d[2] == v and d[3] == v) or 
        (d[4] == v and d[5] == v and d[6] == v) or
        (d[7] == v and d[8] == v and d[9] == v) or
        (d[1] == v and d[4] == v and d[7] == v) or
        (d[2] == v and d[5] == v and d[8] == v) or
        (d[3] == v and d[6] == v and d[9] == v) or
        (d[1] == v and d[5] == v and d[9] == v) or
        (d[3] == v and d[5] == v and d[7] == v)):
         
        return 'Победил первый игрок'


def CheckingStatusO(d):
    v = 'O'
    if ((d[1] == v and d[2] == v and d[3] == v) or 
        (d[4] == v and d[5] == v and d[6] == v) or
        (d[7] == v and d[8] == v and d[9] == v) or
        (d[1] == v and d[4] == v and d[7] == v) or
        (d[2] == v and d[5] == v and d[8] == v) or
        (d[3] == v and d[6] == v and d[9] == v) or
        (d[1] == v and d[5] == v and d[9] == v) or
        (d[3] == v and d[5] == v and d[7] == v)):
         
        return 'Победил второй игрок'


try:
    Graphic(dict)
    for i in range(1, 4):
        MoveFirstPlayer(dict)  # 1
        Graphic(dict)
        for j in range(i, 3):
            MoveSecondPlayer(dict)  # 2
            Graphic(dict)
            break

    if CheckingStatusX(dict) == 'Победил первый игрок':
        print(CheckingStatusX(dict))
    else:
        MoveSecondPlayer(dict)  # 2
        Graphic(dict)
        CheckingStatusO(dict)  # проверка
        if CheckingStatusO(dict) == 'Победил второй игрок':
            print(CheckingStatusO(dict))
        else:
            MoveFirstPlayer(dict)  # 1
            Graphic(dict)
            CheckingStatusX(dict)  # проверка
            if CheckingStatusX(dict) == 'Победил первый игрок':
                print(CheckingStatusX(dict))
            else:
                MoveSecondPlayer(dict)  # 2
                Graphic(dict)
                CheckingStatusO(dict)  # проверка
                if CheckingStatusO(dict) == 'Победил второй игрок':
                    print(CheckingStatusO(dict))
                else:
                    MoveFirstPlayer(dict)  # 1
                    Graphic(dict)
                    CheckingStatusX(dict)  # проверка
                    if CheckingStatusX(dict) == 'Победил первый игрок':
                        print(CheckingStatusX(dict))
                    else:
                        print('Игра окончена. Ничья')
except:
    ValueError: print('Попробуйте еще раз!')

##########################################################################################################