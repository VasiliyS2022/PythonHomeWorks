###############################################################################
def GetEstimation(surname):
    with open('RatingBase.txt', 'r', encoding='utf-8') as file:
        for line in file:
            valueSurname = line.split('*')[0]
            valueDiscipline = line.split('*')[1]
            valueData = line.split('*')[2]
            valueRating = line.split('*')[3]
            if valueSurname == surname:
                print(valueDiscipline + ' - ' + valueData + ' - ' +\
str(valueRating), end='')
    print('\n')
