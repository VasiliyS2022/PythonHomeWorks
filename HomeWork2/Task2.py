# ДОМАШНЕЕ ЗАДАНИЕ СЕМИНАР2 ЗАДАЧА2
##########################################################################################################

# 2) Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.
# Пример:
# Для n = 15: Ответ: 3
# Для n = 35: Ответ: 5

def SmallestDivisor(n):
    for i in range(2, abs(n + 1)):
        if n % i == 0:
            return i

try:
    num = int(input('Введите целое число: '))
    if (num == 1) or (num == (-1)):
        print(f'Для числа {num}, наименьшего натурального делителя, отличного от 1 не существует')
    else:
        print(f'Наименьший натуральный делитель целого числа {num}, отличный от 1 равен {SmallestDivisor(num)}')
except ValueError:
    print('Нужно ввести целое число, попробуйте еще раз!')

##########################################################################################################