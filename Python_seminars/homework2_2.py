# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.#
# Пример:# #
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


list = []
factorial = 1
try:
    digit = int(input('Введите целое число: '))
except ValueError:
    print('Введите целое число больше нуля')
    exit()

if digit > 0:
    for i in range(1, digit + 1):
        factorial *= i
        list.append(factorial)
    print(list)
else:
    print('Введённое число меньше нуля. Введите целое число больше нуля')
