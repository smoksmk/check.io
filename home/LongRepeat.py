#!/usr/bin/python3
# -*- coding: utf-8 -*-

def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    result = 0
    previous_sumbol = ""
    count = 0
    for item in line:
        if previous_sumbol == item:
            count += 1
        else:
            previous_sumbol = item
            count = 1
        if count > result:
            result = count

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    long_repeat("")
    assert long_repeat("abababaab") == 2, "Therd"
    print('"Run" is good. How is "Check"?')
