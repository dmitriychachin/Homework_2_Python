""" 
Требуется вывести все целые степени двойки (т.е. числа
вида 2k
), не превосходящие числа N.
"""

def check_input(massege):

    num = input(massege)

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(0 < int(num)):
                is_correct = True
            else:
                print('У цифры 2 нет такой степени\n')
                num = input(massege)
        else:
            print('Упс :(\n Вы ввели не число, а что-то другое\n')
            num = input(massege)
    return num

N = int(check_input("Введите число\n"))
num = 0
res = 0

while(N > res):
    res = 2**num
    if (res < N):
        print(res)
        num += 1
    else:
        break
