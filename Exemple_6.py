"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в N-мерном пространстве. 
Сначала задается N с клавиатуры, потом задаются координат.
"""

import math

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

N = int(check_input("Введите количество измерений\n"))
first_spot = list()
second_spot = list()

for i in range(N):
    x = int(check_input("Введите координаты первой точки\n"))
    first_spot.append(x)

for i in range(N):
    x = int(check_input("Введите координаты второй точки\n"))
    second_spot.append(x)

sum = 0
for i in range(N):
    sum = sum + (first_spot[i] - second_spot[i]) * 2


if(sum < 0):
    sum = -sum

res = math.sqrt(sum)
print(f"Расстояние между точками равно {res}")