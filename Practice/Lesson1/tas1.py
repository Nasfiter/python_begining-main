# проверить является ли одно число квадратом другого

num_a = int(input('Введите число \na =  '))
num_b = int(input('введите число \nb =  '))

if num_a * num_a == num_b:
    #conclusion = f"Число a {num_a} является квадратом числа b {num_b}"
    print(f"Число a = {num_a} является квадратом числа b = {num_b}")
elif num_b * num_b == num_a:
    print(f"Число b = {num_b} является квадратом числа a = {num_a}")
else:
    print('ниодно из чисел не является квадратом другого')
