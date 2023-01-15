# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работает в обратную сторону - из строки выходных данных, получить строку входных данных.

from collections import Counter

with open("file_digits.txt", "w") as file:
    file.write("111112222334445")


with open("file_digits.txt", "r") as file:
    values = file.read()


def encode(values):

    encoding = ""
    i = 0
    while i < len(values):       
        count = 1

        while i + 1 < len(values) and values[i] == values[i + 1]:
            count += 1
            i += 1      
        encoding += str(count) + values[i]
        i += 1

    return encoding


print(encode(values))

with open("file_digits.txt", "w") as file:
    file.write(encode(values))

with open("file_digits.txt", "r") as file:
    my_str = file.read()

def decode(my_str):
    out = ''
    for i in range (len(my_str)):
        if i % 2 == 0:
            number = int(my_str[i])      
        else:
            for m in range(number):
                out += my_str[i]                
            number = 0  
    return out       
    
print(decode(''.join(my_str)))

with open("file_output.txt", "w") as file:
    file.write(decode(my_str))

with open("file_output.txt", "r") as file:
    my_str = file.read()


# метод декодирования для строк

# def decode(my_str):
#     out = ''
#     number = ''
#     for i in range (len(my_str)):
#         if my_str[i].isdigit():
#             number += my_str[i]      
#         else:
#             # for m in range(number):
#             out += my_str[i]*int(number)                
#             number = ''  
#     return out       
# print(decode(my_str))

# with open("file_output.txt", "w") as file:
#     file.write(decode(my_str))

# with open("file_output.txt", "r") as file:
#     my_str = file.read()


    