# написать программу принимающую 5 чисел и найти макс






# практика 
import random
list_numbers = []
list_numbers = [random.randint(0, 100) for i in range(8) ]
print(f'Рандомные числа {list_numbers}') 

max = list_numbers[0]
for item in list_numbers:
    if max < item:
        max = item
print(f'максимальное число = {max }')