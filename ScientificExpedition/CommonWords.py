#!/usr/bin/python3
# -*- coding: utf-8 -*-

def checkio(first, second):
    result = [world for world in first.split(",") if world in second.split(',')]
    return ','.join(sorted(result))

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"


"""Продолжим изучение слов. 
Даны две строки со словами, разделенными запятыми. 
Попробуйте найти что общего между этими строками. 
Слова внутри каждой строки не повторяются.

Ваша функция должна находить все слова, 
которые появляются в обеих строках. 
Результат должен быть представлен, 
как строка со словами разделенными запятыми и отсортированными в алфавитном порядке.

Вх. данные: Два аргумента как строки (str).

Вых. данные: Общие слова как строка (str).

Предусловия: 
Каждая строка содержит не более 10 слов.
Все слова разделены запятыми.
Все слова состоят только из латинских букв в нижнем регистре."""