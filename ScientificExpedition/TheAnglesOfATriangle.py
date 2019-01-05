#!/usr/bin/python3
# -*- coding: utf-8 -*-
import math

def law(a, b, c):
    return round(math.degrees(math.acos((math.pow(a, 2) + math.pow(b, 2) - math.pow(c, 2))/(2*a*b))))

def checkio(a, b, c):
    line = sorted([a, b, c])
    if line[0] + line[1] <= line[2]:
        return [0, 0, 0]
    else:
        al = law(b, c, a)
        bt = law(a, c, b)
        ga = law(a, b, c)

        return sorted([al, bt, ga])


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"
    assert checkio(5, 4, 3) == [37, 53, 90], "Обратный треугольник"

"""
Даны длины сторон треугольника и необходимо найти углы треугольника. 
Если невозможно сформировать треугольник из данных сторон 
(или для вырожденного треугольника), 
тогда результатом должны быть все нули. 
Результат должен быть представлен, как список (list) 
целых чисел в возрастающем порядке. 
Углы должны быть записаны в градусах и 
округляются до целого числа (стандартное округление).

Входные данные: Длины сторон треугольник, как целые числа (int).

Выходные данные: Углы данного треугольника в градусах, как сортированный список (list) целых чисел (int).

Предусловия: 
0 < a,b,c ≤ 1000
"""