# import colorsys


# colors = ['greeen', 'red', 'blue']
# data = open('data.txt', 'a')
# data.writelines(colors)
# data.write('\nLINE 2\n')
# data.write('LINE 3\n')
# data.close()

# with open('data.txt', 'a') as data:
#     data.write( 'NewLine')


# path = 'data.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()

# from msilib.schema import Directory
# import re
# from symtable import Symbol
# from turtle import clear, right
# from xmlrpc.server import list_public_methods


# def new_string(symbol, count=99):
#     return symbol * count
# print(new_string('!', 6))
# print(new_string('%', 44))
# print(new_string('$'))


# import hello as fc
 
# print(fc.f(2.3))


#######  РЕКУРСИЯ функция вызывающая саму себя. Нужно указывать когда остановиться

##  написать программу которая был складывала следующее число с предыдыущим, шаг 1 , в диапазоне 1 - 10

# def fib(x):
#     if x in [1, 2]:
#         return 1
#     else:
#         return fib(x -1 ) + fib(x-2)
    

# list = []
# for e in range(1, 10):
#     list.append(fib(e))
# print(list)




# a, b = 3, 4
# print(a)
# print(b)
# print(b, a)

######## Кортеж - это неизменяемый список

# a = (1, 3, 5, 9)
# print(a)
# print(type(a))
# print(a[-1])
# print(a[0])

####### СЛОВАРИ это неупорядоченые коллекции с доступом по ключу

# dictionary = {}
# dictionary = \
#     {
#         'left': '<',
#         'right': '>'
#     }

# # print(dictionary['left'])
# # print(dictionary)

# for k in dictionary.values():
#     print(k)

####  МНОЖЕСТВА SET

# EXP

# color = {'red', 'blue', 'green'}
# print(color)
# print(type(color))
