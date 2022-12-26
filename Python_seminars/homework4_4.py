# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

try:
  file = open('task4_4.txt', 'w')      
except FileNotFoundError:
   print('Невозможно открыть файл')

k = int(input('Введите значение степени: '))
if k < 0:
    print('Вы ввели неправильное число! Введите натуральную степень.') 
    exit() 

list = [random.randint(0, 101) for i in range(0, k + 1)]
print(list)

if list[0] == 1:
    file.write(f'x**{k}')
else:    
    file.write(f'{list[0]}x**{k}')    
for i in range(1, k + 1):
    if list[i] != 0:        
        if list[i] > 0:
            file.write(' + ')
        if list[i] != 1:                       
            file.write(f'{list[i]}')                     
        if i != k and i != k-1:
            file.write(f'x**{k-i}')
        elif i == k - 1:
            file.write('x')
file.write(' = 0')   
   
file.close()