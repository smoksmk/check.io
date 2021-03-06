#!/usr/bin/python3
# -*- coding: utf-8 -*-

fibo = {0: True}

def fib(a):
    if a in fibo:
        return fibo[a]
    else:
        fib_prev, fib_next = 0, 1
        n = 1
        while fib_next <= a:
            if fib_next not in fibo: fibo[a] = True
            if fib_next == a:
                return True
            fib_prev, fib_next = fib_next, fib_prev + fib_next
            n += 1
        else:
            fibo[a] = False
            return False

def checkio(opacity):
    life = 10000
    for i in range(5000):
        if fib(i):
            life -= i
        else:
            life += 1
        if life == opacity:
            return i




#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':

    assert checkio(10000) == 0, "Newborn"
    assert checkio(9999) == 1, "1 year"
    assert checkio(9997) == 2, "2 years"
    assert checkio(9994) == 3, "3 years"
    assert checkio(9995) == 4, "4 years"
    assert checkio(9990) == 5, "5 years"
    print(fibo)
    print("Check Success")


"""У Николы появилось свободное время и он решил заняться исследованием привидений. 
Он хочет найти способ, как определять возраст привидений. 
Согласно древним фолиантам, возраст связан со степенью прозрачности призраков.
Никола составил шкалу измерений прозрачности от 10000 до 0, 
где 10000 - это совсем не прозрачное "новорождённое" привидение (0 лет) и 0 - это уже невидимка (возраст неизвестен).

После множества экспериментов, Никола кажется нашел взаимосвязь.
На каждый "день рождения", степень прозрачности привидения уменьшается на количество единиц,
равное его возрасту, если возраст есть одно из чисел Фибоначчи, иначе увеличивается на единицу.

Для примера:
"Новорождённое" привидение -- 10000 единиц прозрачности.
1 год -- 10000 - 1 = 9999 (1 число Фибоначчи).
2 года -- 9999 - 2 = 9997 (2 число Фибоначчи).
3 года -- 9997 - 3 = 9994 (3 число Фибоначчи).
4 года -- 9994 + 1 = 9995 (4 не число Фибоначчи).
5 лет -- 9995 - 5 = 9990 (5 число Фибоначчи).
Помогите Николе написать функцию, которая будет определять возраст привидения по прозрачности. 
Вам известно измерение прозрачности, как число от 0 до 10000 включительно. Привидения не бывают старше 5000 лет, так как потом просто исчезают (серьезно, научный факт).

Эта задача посвящена Хэллоуину и поэтому мы ждем от вас "волшебных" или "страшных" решений.

Входные данные: Степень прозрачности, как целое число.

Выходные данные: Возраст привидения, как целое число.

Предусловия:
age < 5000
0 < opacity ≤ 10000"""

# for n in range(10):
#     i = n*(n + 1) / 2
#
#     y = (pow(8*i+1, 0.5)-1)/2

# print("n=", n, "i=", i, "y=", y)
