# программа в которой вводишь число и она выдает список от -N до +N 

n = int(input('Ведите целлое число = '))

if n < 0:
    n = - n
list_of_n = []
for items in range(-n, n+1):
    list_of_n.append(items)
print(list_of_n)