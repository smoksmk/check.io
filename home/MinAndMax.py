#!/usr/bin/python3
# -*- coding: utf-8 -*-


def min(args1, *args, **kwargs):

    key = kwargs.get("key", lambda x : x)

    if args:
        iterable = [args1] + list(args)
    else:
        iterable = list(args1)

    result = iterable[0]
    for item in iterable[1:]:
        if key(item) < key(result):
            result = item

    return result


def max(args1, *args, **kwargs):

    key = kwargs.get("key", lambda x : x)
    if args:
            iterable = [args1] + list(args)
    else:
        iterable = list(args1)
    result = iterable[0]

    for item in iterable[1:]:

        if key(item) > key(result):
            result = item

    return result



if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    assert min((9,)) == 9, 'не олжно вровзвращать в скобках'
    print(min(abs(i) for i in range(-10, 10)))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")