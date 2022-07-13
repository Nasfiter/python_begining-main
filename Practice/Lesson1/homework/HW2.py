# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):

            left_part_equation = not(x and y and y)
            right_part_equation = -x or -y or -z 
            print(x, y, z, left_part_equation == right_part_equation)



