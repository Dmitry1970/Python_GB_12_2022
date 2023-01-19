# Задача 32:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

number = int(input("Введите число: "))
pow = int(input("Введите степень: "))


def recur(number, pow):
    if pow == 1:
        return number
    if pow != 1:
        return number * recur(number, pow - 1)


print(recur(number, pow))
