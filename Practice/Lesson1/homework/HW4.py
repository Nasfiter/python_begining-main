# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


from msilib.schema import Error
import queue
from turtle import clear


quater = int(input('Введите № четверти х/y: '))
range_list = {1, 2, 3, 4}
if quater// 10 ==0 and quater >=1 and quater <=4:
    print('Четверть выбрана правильно')
if quater == 1:
    print('Координаты в диапазоне x(0, oo) y(0, oo)')
elif quater == 2:
    print('Координаты в диапазоне x(0, -oo) y(0, oo)')
elif quater == 3:
    print('Координаты в диапазоне x(0, -oo) y(0, -oo)')
elif quater == 4:
    print('Координаты в диапазоне x(0, oo) y(0, -oo)')


else:
    print('Error')
   
        
        