# для натуральных n создать словарь индекс-значенияб состоящий из элементов последовательности 3n + 1
# EXP для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

num = int(input(' Inter nu: '))
list_l = []
for i in range(num + 1):
    list_l.append(3*i + 1)
print(list_l)
