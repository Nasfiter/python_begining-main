# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}

number = int(input('Inter an integer: '))

list_product = []
for i in range(1, number + 1):
    list_product.append((1+1/i)**i)
#print(type(list_product))
print(list_product)

sum = 0
for item in list_product:
    sum = sum + item

print('Sum of all elements in the list: ',sum)