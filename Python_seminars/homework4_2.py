# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

number = int(input('Введите число: '))
multi_range = int(number**0.5)
list_multi = []
for i in range(2, multi_range + 1):
    while  number % i == 0:  
        list_multi.append(i)       
        number /= i                
if(number > 1):
    list_multi.append(int(number)) 
print(list_multi)