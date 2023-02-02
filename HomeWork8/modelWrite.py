###############################################################################
def SetRating(surname, discipline, data, rating):
    with open('RatingBase.txt', 'a', encoding='utf-8') as file:
            file.write('\n')
            file.write(surname + '*' + discipline + '*' + data + '*' +\
 str(rating))