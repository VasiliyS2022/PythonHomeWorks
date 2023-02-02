###############################################################################
import modelRead as m1
import modelWrite as m2
import view

def Button_click():
    while(True):
        selectRole = view.GetSelectRole()
        if selectRole == 1:
            while(True):
                selectAction = view.GetSelectActionTeacher()
                if selectAction == 1:
                    surname = view.GetSurname()
                    discipline = view.GetDiscipline()
                    data = view.GetData()
                    rating = view.GetRating()
                    m2.SetRating(surname, discipline, data, rating)
                if selectAction == 2:
                    surname = view.GetSurname()
                    m1.GetEstimation(surname)
                if selectAction == 3:
                    break
        if selectRole == 2:
            while(True):
                selectAction = view.GetSelectActionStudent()
                if selectAction == 1:
                    surname = view.GetSurname()
                    m1.GetEstimation(surname)
                if selectAction == 2:
                    break
        if selectRole == 3:
            break
        