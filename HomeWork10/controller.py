from calc import addition, subtraction, multiplication, division

def parsing_values(values):                                             
    action = []                  
    sign = []
    for i in values:
        if i.isdigit():
            sign.append(i)
        elif (not i.isdigit()) and sign:
            action.append(int(''.join(sign)))
            action.append(i)
            sign = []
        elif (not i.isdigit()) and (not sign):
            action.append(i)
    if sign:
        action.append(int(''.join(sign)))
    return action

def calculate(equation):                                       
    res = 0
    if len(equation) == 1:
        return equation[0]
    for s in equation:
        if s == '*' or s == '/':
            if s == '*':
                x = equation.index(s)
                res = multiplication(equation[x - 1], equation[x + 1])
                equation = equation[:x - 1] + [res] + equation[x + 2:]
            else:
                x = equation.index(s)
                res = division(equation[x - 1], equation[x + 1])
                equation = equation[:x - 1] + [res] + equation[x + 2:]
    for s in equation:
        if s == '+' or s == '-':
            if s == '+':
                x = equation.index(s)
                res = addition(equation[x - 1], equation[x + 1])
                equation = equation[:x - 1] + [res] + equation[x + 2:]
            else:
                x = equation.index(s)
                res = subtraction(equation[x - 1], equation[x + 1])
                equation = equation[:x - 1] + [res] + equation[x + 2:]
    return res

def solution_equation(lst):                                     
    flag = 1
    while flag == 1:
        if ')' in lst:
            for i in range(lst.index(')'), -1, -1):
                if lst[i] == '(':
                    ix = lst.index(')')
                    elem = calculate(lst[i + 1:ix])
                    lst = lst[:i] + [elem] + lst[ix + 1:]
        elif ')' not in lst:
            flag = 0
    return calculate(lst)