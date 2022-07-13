# написать программу, которая принимает дробное число и которая будет выводить только десятичное значегние 
 
from numbers import Number
from unicodedata import decimal


nm = float(input('Введите число \na = '))
#print(number) 

num_other = nm * 10 

#print(num_other)

num_other = int(num_other)

#print(num_other)

num_other = str(num_other)

#print(type(num_other))

print(num_other[-1])