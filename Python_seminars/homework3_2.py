# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random

number = int(input('Введите число: '))
list = []

for i in range(number):
    list.append(random.randint(0, 10))
print(list)

multiList = []
for i in range(int(number//2 + len(list) % 2)):
    multiList.append(list[i] * list[number - 1 - i])
print(multiList)
