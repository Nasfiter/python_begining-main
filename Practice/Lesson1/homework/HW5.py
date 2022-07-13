# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21



coordinates_X1 = float(input('Введите координаты Х1: '))
coordinates_X2 = float(input('Введите координаты Х2: '))
coordinates_Y1 = float(input('Введите координаты Y1: '))
coordinates_Y2 = float(input('Введите координаты Y2: '))

interval = ((coordinates_X2 - coordinates_X1)**2 + (coordinates_Y2 - coordinates_Y1)**2)**0.5

print('Растояние между 2-мя точками = ',interval)