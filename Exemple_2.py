"""
Петя и Катя – брат и сестра. Петя – студент, а Катя –
школьница. Петя помогает Кате по математике. Он задумывает два
натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
этого Петя делает две подсказки. Он называет сумму этих чисел S и их
произведение P. Помогите Кате отгадать задуманные Петей числа.
"""

def check_input(massege):

    num = input(massege)

    is_correct = False
    while(is_correct == False):
        if (num.isdigit()):
            if(0 < int(num) <= 1000):
                is_correct = True
            else:
                print('Похоже вы не поместились в пределы, число должно быть больше 0 и мнеьше или равно 1000\n')
                num = input(massege)
        else:
            print('Упс :(\n Вы ввели не число , а что-то другое\n')
            num = input(massege)
    return num

num1 = int(check_input("Введите сумму двух чисел\n"))
num2 = int(check_input("Введите произведение двух чисел\n"))
res = list()

if(num1 > num2):
    ran = num1
else:
    ran = num2

for x in range(1, int(num1/2)+1):
        y = num1 - x
        if x * y == num2:
            res.append(x)
            res.append(y)

if res:
    print("Эти числа загодал Петя", res)
else:
    print("Походу Петя ошибся и под такие числа ничего не подходит")
