# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# ¬  not(отрицаниеб инверсия);
# ⋁  or(логическое сложение, дизъюнкция);
# ⋀  and(логическое умножение, конъюнкция);

print('======= 1-й способ ========')

print('x y z')
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            print(x, y, z, end="    ")
            if not (x or y or z) == (not x and not y and not z):
                print('True')
            else:
                print('False')


print('======= 2-й способ ========')

print('x y z')
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, end="    ")
            if not (x or y or z) == (not x and not y and not z):
                print('True')
            else:
                print('False')
