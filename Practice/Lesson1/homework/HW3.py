# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coordinate_x = float(input('Введите координату x = '))
coordinate_y = float(input('Введите координату y = '))

if coordinate_x !=0 and coordinate_y !=0: 
    print()
else: print('Введите другие числа отличительные от 0 ')
if coordinate_x > 0 and coordinate_y > 0:
    print('четверть: 1 ')
elif coordinate_x > 0 and coordinate_y < 0:
    print('четверь: 4 ')
elif coordinate_x < 0 and coordinate_y > 0: 
    print('четверть: 2')
elif coordinate_x < 0 and coordinate_y < 0:
    print('четверть 3:')