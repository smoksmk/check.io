# def checkio(pas):
#
#     if len(pas) < 10:
#
#         return False
#
#     numbers = sum(c.isdigit() for c in pas)
#
#     upper_str = sum(c.isupper() for c in pas)
#
#     lower_str = sum(c.islower() for c in pas)
#
#     return True if (upper_str > 0) and (lower_str > 0) and (numbers > 0) else False
#
# #Some hints
#
# #Just check all conditions
#

def checkio(data):
    print("-----------------------")
    print('Первое условие', len(data))

    if len(data) < 10:
        return False

    print ("Второе условине", {True for i in data if i.isnumeric()})
    if not {True for i in data if i.isnumeric()}:
        return False
    print("третье условине", {True for i in data if i.isupper()})
    if not {True for i in data if i.isupper()}:
        return False
    print("четвертое условине", {True for i in data if i.isalpha()})
    if not {True for i in data if i.isalpha()}:
        return False
    if not {True for i in data if i.islower()}:
        return False

    return True

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("erer798rew9rew9r7ew987rw") == False, 'NEW'
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"

    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
