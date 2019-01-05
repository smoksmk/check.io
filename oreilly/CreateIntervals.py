#!/usr/bin/python3
# -*- coding: utf-8 -*-

def create_intervals(data):

    data = sorted(data)
    first = 0
    result = []

    for i in range(len(data)):

        try:
            if data[i+1] != data[i]+1:
                result.append((data[first], data[i]))
                first = i+1

        except:
            result.append((data[first], data[i]))

    return result

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
