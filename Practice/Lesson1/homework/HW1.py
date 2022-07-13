# 1- Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day_of_the_week = float(input('Введите число соответствующее дню недели = '))
#print(type(day_of_the_week))
#num = day_of_the_week
if (day_of_the_week * 10 % 10) == 0:        # проверка если число целое
    day_of_the_week = int(day_of_the_week)  # перевод из float to int
    #print(day_of_the_week)                  # проверка 
if day_of_the_week >= 1 and day_of_the_week <=5:
    print('Увы не выходной ')
elif day_of_the_week == 6 or day_of_the_week == 7:
    print('ура! Выходной!!!')
else:
    print('Введите число от 1 до 7')




