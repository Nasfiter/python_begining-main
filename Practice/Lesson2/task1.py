# Написать программу, которая принимает на вход число № и выдает последовательность из № члено
# приме: Дл № = 5: 1, -3, 9, -27, 81

num = int(input('inter an integer: '))

result = 1
for i in range(num):
    print(result, end = ' ')
    result *= -3


    