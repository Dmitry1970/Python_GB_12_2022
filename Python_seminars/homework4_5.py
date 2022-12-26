# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import random

try:
    file1 = open('file1.txt', 'w')
except FileNotFoundError:
    print('Невозможно открыть файл')

try:
    file2 = open('file2.txt', 'w')
except FileNotFoundError:
    print('Невозможно открыть файл')

try:
    file3 = open('file3.txt', 'w')
except FileNotFoundError:
    print('Невозможно открыть файл')


k1 = int(input('Введите значение степени k1: '))
if k1 < 0:
    print('Вы ввели неправильное число! Введите натуральную степень.')
    exit()

k2 = int(input('Введите значение степени k2: '))
if k2 < 0:
    print('Вы ввели неправильное число! Введите натуральную степень.')
    exit()

list1 = [random.randint(0, 101) for i in range(0, k1 + 1)]
print(list1)

if list1[0] == 1:
    file1.write(f'x**{k1}')
else:
    file1.write(f'{list1[0]}x**{k1}')
for i in range(1, k1 + 1):
    if list1[i] != 0:
        if list1[i] > 0:
            file1.write(' + ')
        if list1[i] != 1:
            file1.write(f'{list1[i]}')
        if i != k1 and i != k1-1:
            file1.write(f'x**{k1-i}')
        elif i == k1 - 1:
            file1.write('x')
file1.write(' = 0')

list2 = [random.randint(0, 101) for i in range(0, k2 + 1)]
print(list2)

if list2[0] == 1:
    file2.write(f'x**{k2}')
else:
    file2.write(f'{list2[0]}x**{k2}')
for i in range(1, k2 + 1):
    if list2[i] != 0:
        if list2[i] > 0:
            file2.write(' + ')
        if list2[i] != 1:
            file2.write(f'{list2[i]}')
        if i != k2 and i != k2-1:
            file2.write(f'x**{k2-i}')
        elif i == k2 - 1:
            file2.write('x')
file2.write(' = 0')

list3 = []
x = 'x'
if k1 > k2:
    for i in range(k2+1):
        list3.insert(0, list1[len(list1) - 1 - i] + list2[len(list2) - 1 - i])
print(list3)

for i in range(k1 - k2):
    file3.write(f'{list1[i]}x**{k1 - i} + ')

for i in range(len(list3)):
    if i == 0:
        file3.write(f'{list3[i]}x**{len(list3)-1}')
    elif i > 0 and i < len(list3) - 2:
        file3.write(f' + {list3[i]}x**{len(list3)- 1- i}')
    elif i == len(list3) - 2:
        file3.write(f' + {list3[i]}x')
    elif i == len(list3) - 1:
        file3.write(f' + {list3[len(list3)-1]}')

# 84x**5 + 11x**4 + 180x**3 + 43x**2 + 81x + 96 = 0


file3.write(' = 0')


#
#
#     else:
#         file3.write(f' + {list3[len(list3) - 1 - i]}x**{(len(list3) - i)}')
# print(f'{list3[len(list3)-1-i]}x**{(len(list3)-1-i)}')

# if k1 > k2:
#     while k1 - k2 != 0:
#         for i in range(k2 + 1):
#             for i in range(k1 + 1):
#                 list3.append(list1[len(list1)-i] + list2[len(list2) - j])
#         k1 -=1
#         k2 -=1


file1.close()
file2.close()
file3.close()
