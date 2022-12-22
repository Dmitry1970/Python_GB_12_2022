# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
#
# Пример:
#
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

size = int(input('Ввведите размер списка: '))
list = []

for i in range(size):
    list.append(round(random.random()*10, 2))
print(list)

newList = []
difference = 0
for i in list:
    newList.append(round(i * 100) % 100)
print(newList)
difference = (max(newList) - min(newList))/100
print(difference)

# 2-ой способ

newList = []
difference = 0
for i in list:
    newList.append(round(i * 100) % 100)
print(newList)

max = 0
min = 100
for i in newList:
    if max < i:
        max = i
    if min > i:
        min = i
difference = (max - min)/100
print(difference)
