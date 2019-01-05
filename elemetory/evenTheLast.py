def checkio(array):
    """
        sums even-indexes elements and multiply at the last

        return 0 if array == [] else sum(array[::2]) * array[-1]
    """
    result = 0
    cout = len(array)
    if cout != 0:
        for i in range(0, cout):
            if not i%2:
                result = result+array[i]

        result = result*array[-1]
    else:
        result = 0

    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")