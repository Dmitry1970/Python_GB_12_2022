# Реализуйте алгоритм перемешивания списка.

import random

size = int(input('Ввведите размер списка: '))
list = []
a = 1
b = 11
for i in range(size):
    list.append(random.randint(a, b))
print(list)

random.shuffle(list)        # сортировка с помощью метода shuffle
print(f'Перемешивание списка методом shuffle(): {list}')


# Сортировка перемешиванием(модификация сортировки пузырьком)

left = 0
right = len(list) - 1
control = right                 # контроль факта обмена
while left < right:
    for i in range(left, right):
        if list[i] > list[i+1]:
            list[i], list[i+1] = list[i+1], list[i]
            control = i
    right = i
    for i in range(right, left, -1):
        if list[i] < list[i-1]:
            list[i], list[i-1] = list[i-1], list[i]
            control = i
    left = control

print(f'Перемешивание списка(коктейльная сортировка): {list}')
