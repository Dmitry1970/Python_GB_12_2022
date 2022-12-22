# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# моё решение

n = int(input('Введите число: '))
list1 = []
list1.append(0)
list1.append(1)
for i in range(n - 1):
    list1.append(list1[-2] + list1[-1])
list1.pop(0)

list2 = []
list2.append(0)
list2.append(1)
for i in range(n - 1):
    list2.append(list2[-2] - list2[-1])   
list2.reverse()

print(list2 + list1)


# решение на семинаре

# def postive_fib(n):
#     postive_list = [0,1]
#     for i in range(n-1):
#         postive_list.append(postive_list[-2]+postive_list[-1])
#     return postive_list
#
# def negative_fiv(n):
#     negative_list = [0,1]
#     for i in range(n-1):
#         negative_list.append(negative_list[-2]-negative_list[-1])
#     return negative_list
#
#
# print(negative_fiv(8)[::-1] + postive_fib(8)[1:])
