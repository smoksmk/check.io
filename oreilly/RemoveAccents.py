#!/usr/bin/python3
# -*- coding: utf-8 -*-

def checkio(in_string):
    "remove accents"
    test = ["préfèrent", "preferent"]
    for i in test[0]:
        print(ord(i))

    print()
    for i in test[1]:
        print(ord(i))

    return in_string

    # These "asserts" using only for self-checking and not necessary for auto-testing


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
