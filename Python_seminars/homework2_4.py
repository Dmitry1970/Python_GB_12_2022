# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.


try:
   file = open('Python_seminars\myText.txt')       
except FileNotFoundError:
   print('Невозможно открыть файл')

f = file.read().splitlines()
index = 0
indexList = []
for i in f:
    indexList.append(int(i))
print(indexList) 

n = int(input('Введите число: '))
list = []
for i in range(2*n + 1):   
    list.append(-n + i)   
print(list)

changedList = []
for i in range(2*n + 1):   
    changedList.append(-n + i)   
    for j in range(len(indexList)):       
        if indexList[j] == i:                  
            changedList[i] *= indexList[j] 
        else:
            continue    
print(changedList)   

file.close()



