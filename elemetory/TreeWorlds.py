def checkio(words):
    data = words.split(' ')
    count = 0
    for value in data:
        if value.isalpha():
            count += 1
            if count >= 3: return True
        else: count = 0

    return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True, "Hello"
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
