###############################################################################
def GetSelectRole():
    return int(input('Выберите роль:\n 1 - Учитель\n 2 - Ученик\n \
3 - Выход\n'))

def GetSelectActionTeacher():
    return int(input('Выберите действие:\n 1 - Поставить оценку\n \
2 - Посмотреть оценку\n 3 - Выход\n'))

def GetSelectActionStudent():
    return int(input('Выберите действие:\n 1 - Посмотреть оценку\n \
2 - Выход\n'))

def GetSurname():
    return input('Введите фамилию и инициалы в формате "Фамилия И.О" \
без кавычек: ')

def GetDiscipline():
    return input('Введите учебную дисциплину: ')

def GetData():
    return input('Введите дату в формате ДД.ММ.ГГ: ')

def GetRating():
    return int(input('Введите оценку от 1 до 5: '))
