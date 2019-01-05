#!/usr/bin/python3
# -*- coding: utf-8 -*-

def show_pawns(pawns):
    print("  abcdefgh")
    for x in reversed(range(1, 9)):
        line_y = ""
        for y in "abcdefgh":
            if str(y)+str(x) in pawns:
                line_y += "♙"
            else:
                line_y += "."
        print(x, line_y)

def safe_pawns(pawns):
    show_pawns(pawns)
    count = 0
    for i in pawns:
        if str(chr(ord(i[0])-1)) + str(int(i[1])-1) in pawns or str(chr(ord(i[0])+1)) + str(int(i[1])-1) in pawns:
            count += 1

    return count




if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    try:
        assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
        assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
        print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
    except AssertionError:
        print("Проверка не пройдена")

    print(abs(i) for i in range(-10, 10))
