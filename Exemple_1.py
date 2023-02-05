"""
На столе лежат n монеток. Некоторые из них лежат вверх
решкой, а некоторые – гербом. Определите минимальное число
монеток, которые нужно перевернуть, чтобы все монетки были
повернуты вверх одной и той же стороной. Выведите минимальное
количество монет, которые нужно перевернуть.
"""

from random import randint

def check_input(massege):

    num = input(massege)

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(0 < int(num)):
                is_correct = True
            else:
                print('Похоже вы потратили все монеты\n')
                num = input(massege)
        else:
            print('Упс :(\n Вы ввели не число монет, а что-то другое\n')
            num = input(massege)
    return num

num = int(check_input("Введите количество монет\n"))
table = list()
count0 = 0
count1 = 1

for i in range(num):
    x = randint(0,1)
    table.append(x)

for i in range(num):
    if (table[i] == 0):
        count0 += 1
    else:
        count1 += 1

print(table)

if (count0 > count1):
    print(f"Нужно перевернуть {count1} монет")
else:
    print(f"Нужно перевернуть {count0} монет")
