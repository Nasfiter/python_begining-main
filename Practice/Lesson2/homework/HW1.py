# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

from ast import Slice


number = float(input('Enter the number: '))
into_int_number =int(number)
into_Str_number = str(into_int_number)
list_number = list(into_Str_number)
#print(type(into_list_number))N|
print(list_number)
# size = len(into_list_number)
# print('Length of the list: ', size)

new_list = []
for i in list_number:
    
print(new_list)
#print(type(new_list))


sum = 0
for item in new_list:
    sum = sum + item
print('Sum of all digits: ',sum)
