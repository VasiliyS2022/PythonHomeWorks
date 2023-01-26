def WriteValuesColumn(values):
    with open('1.txt', 'a', encoding='utf-8') as file:
        file.write(f'Фамилия: {str(values[0])},  Имя: {str(values[1])}, Телефон: {str(values[2])}, Описание: {str(values[3])} \n')

def WriteValuesRow(values):
    with open('2.txt', 'a', encoding='utf-8') as file:
        file.write(f'Фамилия: {str(values[0])} \nИмя: {str(values[1])} \nТелефон: {str(values[2])} \nОписание: {str(values[3])} \n\n')