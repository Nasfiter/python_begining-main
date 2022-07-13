

#            переменные 
# int, float, boolean, str, list, none

# value = None # просто пустую переменню нельзя вводить. поэтому можно ее заполнить значением None
# print(type(value))
# a = 123
# print(type(a))
# b = 1.23
# print(a)
# print(b)
# value = 143242
# print(type(value))
# print(value)

# что бы указать строку то текст должен быть в кавычках 
# a = 'Hello Python'
# print(a)
# print(type(a))

# разные способы вывода 

# a = 30 
# b = 40
# c = 70
# print(a, b, c)
# print('{} + {} = {}'.format(a, b, c))
# print('{1} + {0} = {2}'.format(a, b, c))
# print(f'{a} + {b} = {c}')

# списки задаются в []

# num = [1, 50, 0.9 ]
# print(num)
# print(type(num))


# ВВОД И ВЫВОД ДАННЫХ ПРЕОБРАЗОВАНИЕ ТИПОВ

# a = int(input('Введите число \na = '))
# print(type(a))
# print('введите число\nb')
# b = int(input())
# #print(a + b)
# # print(f'{a} + {b} = ')
# # print(a + b)
# print('a + b = ', a + b)

#   АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ
# +, -, *, /, %, //, **

# a = 1.3 
# b = 3
# c = round(a * b, 2)
# print(c)
# print(round(a * b,3) )

#   ЛОГИЧЕСКИЕ ОПЕРАЦИИ    >, <, >=, <=, ==, !=, not, and, or

#    управляющие конструкции: if, if-else

# for i in 1, 2, 3, 4: 
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)


# строки 

# text = 'различные манипуляции с текстом'  
# print(len(text))                 # показывает скольк символов в строке включая пробелы
# print('разли' in text)       #  показывает если ли то или иной элемент в строке
# print(text.isdigit())             
# print(text.islower())
# print(text.replace('р', 'Р'))


# ФУНКЦИИ

# from ast import arg


# def f(x): 
#     if x ==1:
#         return "целое"
#     elif x == 2.3:
#         return 23
#     else:
#         return
# arg = 2 
# print(f(arg))
# print(type(f(arg))) 
