"""
Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

*Пример:*

для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
"""

def check_input(massege):

    num = input(massege)

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(0 < int(num)):
                is_correct = True
            else:
                print('Похоже вы ввели не число\n')
                num = input(massege)
        else:
            print('Упс :(\n Вы ввели не число, а что-то другое\n')
            num = input(massege)
    return num

num = int(check_input("Введите количество чисел в формуле Фибоначчи, не считая нуля\n"))


def Fibonachi(num):
    table = [1, 0, 1]
    i = 2
    while i < num:
        fib_sum = table[- 1] + table[ - 2]
        table.append(fib_sum)
        if (i % 2 == 0):
            table.insert(0, -fib_sum)
        else:
            table.insert(0, fib_sum)
        i = i + 1
    return table      

fibonachi = Fibonachi(num)
print(fibonachi)