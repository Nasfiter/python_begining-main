# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input('Inter an integer:  '))
product = 1

if number != 0:
    for item in range(1, number + 1):
        product = product * item

print('n! = ',product)