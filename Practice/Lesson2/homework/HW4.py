# Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности
import random
array_list = [i for i in input('Inter data: ').split(',')]
print(array_list)

array_list_length = len(array_list)
print('Array Length:' ,array_list_length)

# ######################################
# # experementing to find a solution
# #print(type(array_list_length))
# # a = random.randint(0, 10)
# # print(a)

# # a = random.randint(0, array_list_length)
# # print(a)

# # list_b = [None]* array_list_length
# # print(list_b)
# #####################################
for i in range(array_list_length):
     a = random.randint(0, (array_list_length-1))
     print('a= ',a)
     item = array_list.pop(a)
     array_list.append(item)
print('Shuffled List: ', array_list )

