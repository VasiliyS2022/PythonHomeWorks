import modelRead as m1
import modelWrite as m2
import view

def Button_click():
    while(0 < 1):
        selectStart = view.GetSelectStart()
        if selectStart == 1:
            selectView =  view.GetSelectView()
            try:
                if selectView == 1:
                    m1.ViewColumn()
                elif selectView == 2:
                    m1.ViewRow()
            except FileNotFoundError:
                print('Справочник пустой')
        elif selectStart == 2:
            valueSurname = view.GetSurname()
            valueName = view.GetName()
            valueTelephone = view.GetTelephone()
            valueDescription = view.GetDescription()
            listValues = [valueSurname, valueName, valueTelephone, valueDescription]
            m2.WriteValuesColumn(listValues)
            m2.WriteValuesRow(listValues)
        elif selectStart == 3:
            break