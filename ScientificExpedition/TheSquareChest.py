#!/usr/bin/python3
# -*- coding: utf-8 -*-

def print_pow(lines_list):
    i = 0
    flagx = True
    flagy = True
    flagxy = False
    line = list()
    for x in range(7):
        line.append(list())
        if flagx:
            flagx = not flagx
            for y in range(8):
                if flagy:
                    flagy = not flagy
                    i += 1
                    line[x].append(str(i))
                else:
                    flagy = not flagy
                    if [i, i+1] in lines_list:
                        line[x].append("-")
                    else:
                        line[x].append(" ")

            print(" ".join(line[x]))

        else:
            flagx = not flagx
            for yx in range(8):
                if flagxy:
                    flagxy = not flagxy
                    line[x].append(" ")
                else:
                    flagxy = not flagxy
                    line[x].append("|")
            print(" ".join(line[x]))

def checkio(lines_list):
    """Return the quantity of squares"""
    print_pow(lines_list)

    return 0


if __name__ == '__main__':
    assert (checkio([[1, 2], [3, 4], [1, 5], [2, 6], [4, 8], [5, 6], [6, 7],
                     [7, 8], [6, 10], [7, 11], [8, 12], [10, 11],
                     [10, 14], [12, 16], [14, 15], [15, 16]]) == 3), "First, from description"
    assert (checkio([[1, 2], [2, 3], [3, 4], [1, 5], [4, 8],
                     [6, 7], [5, 9], [6, 10], [7, 11], [8, 12],
                     [9, 13], [10, 11], [12, 16], [13, 14], [14, 15], [15, 16]]) == 2), "Second, from description"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 6]]) == 1), "Third, one small square"
    assert (checkio([[1, 2], [1, 5], [2, 6], [5, 9], [6, 10], [9, 10]]) == 0), "Fourth, it's not square"
    assert (checkio([[16, 15], [16, 12], [15, 11], [11, 10],
                     [10, 14], [14, 13], [13, 9]]) == 0), "Fifth, snake"


"""
Панель представляет собой решетку из пронумерованных точек. 
Решетка состоит из прямоугольной матрицы точек и линий, 
соединяющих некоторые пары близлежащих точек. 
Решением является код, равный количеству квадратов, 
образованных линиями. Например, 
на фигуре, представленной ниже, 
есть три квадрата: два малых и один средний.
"""