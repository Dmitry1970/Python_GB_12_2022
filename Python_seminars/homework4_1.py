# Вычислить число c заданной точностью d
# Пример:
#
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# 1-й способ

import math


d = int(input('Введите точность числа(количество знаков после запятой: '))
result = round(math.pi, d)
print(result)
