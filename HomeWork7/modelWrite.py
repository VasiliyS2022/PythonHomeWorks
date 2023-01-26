def WriteValuesColumn(values):
    with open('1.txt', 'a') as file:
        file.write(f'Фамилия: {str(values[0])},  Имя: {str(values[1])}, Телефон: {str(values[2])}, Описание: {str(values[3])} \n')

def WriteValuesRow(values):
    with open('2.txt', 'a') as file:
        file.write(f'Фамилия: {str(values[0])} \n  Имя: {str(values[1])} \n Телефон: {str(values[2])} \n Описание: {str(values[3])} \n\n')