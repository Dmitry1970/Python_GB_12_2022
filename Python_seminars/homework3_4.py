# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# Пример:
#
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input('Введите число: '))
list = []
while number >= 1:
    if number % 2 == 0:
        list.append(number % 2)
    else:
        list.append(number % 2)
        number -= 1
    number = number//2
list.reverse()
result = 0
for i in list:
    result = result * 10 + i
print(result)


# решение на семинаре

# def dec_to_bin(num, result = ""):
#     if num == 0:
#         return result[::-1]
#     result += str(num%2)
#     return dec_to_bin(num//2,result)
#
#
# n = int(input())
#
# if n!=0:
#     print(dec_to_bin(n))
# else:
#     print(0)
