#!/usr/bin/python3
# -*- coding: utf-8 -*-

import numpy as np

def getList(data):
    result = list()
    for i in range(len(data)):
        result.append([data[i][n] for n in range(len(data[i]))])
    return result


def recall_password(cipher_grille, ciphered_password):

    maps = getList(cipher_grille)
    matrixs = getList(ciphered_password)
    data = list()

    for rotate in range(4):
        mass = np.rot90(maps, rotate, axes=(1, 0))
        for x in range(len(mass)):
            for y in range(len(mass[x])):
                if mass[x][y] == "X":
                    data.append(matrixs[x][y])

    return ''.join(data)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'


"""Помогите Софи написать дешифратор для паролей,
которые Никола зашифровал с помощью шифровальной решетки. 
Шифрорешетка - это квадрат 4 на 4 с четырьмя вырезанными окошками. 
Поместите решетку на листе бумаги такого же размера с буквами, 
выписываете первые 4 символа, которые видно в окошках (см. рисунок). 
Затем поверните решетку на 90 градусов по часовой стрелке. 
Выпишите следующие символы и повторите поворот. 
В итоге процедура повторяется 4 раза. 
Таким образом сложно узнать пароль без специальной решетки.

Напишите программу, которая поможет проводить данную процедуру.

Шифровальная решетка и зашифрованный пароль представлены, как массив строк.

Входные данные: Шифровальная решетка и зашифрованный пароль, как список (list) строк.

Выходные данные: Пароль, как строка.

Предусловия: len(cipher_grille) == 4
len(ciphered_password) == 4
all(len(row) == 4 for row in ciphered_password)
all(len(row) == 4 for row in cipher_grille)
all(all(ch in string.ascii_lowercase for ch in row) for row in ciphered_password)
all(all(ch == "X" or ch == "." for ch in row) for row in cipher_grille)"""