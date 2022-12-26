# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random

sequence = [random.randint(0, 20) for i in range(random.randint(0, 20))]
print(sequence)
seq = set(sequence)
print(seq)

# 2-ое решение

sequence_2 = [random.randint(0, 20) for i in range(random.randint(0, 20))]
print(sequence_2)

sequence_list = []
for i in sequence_2:
    if i not in sequence_list:
        sequence_list.append(i)

sequence_list.sort()
print(sequence_list)
