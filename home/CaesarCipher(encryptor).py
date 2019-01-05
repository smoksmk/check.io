#!/usr/bin/python3
# -*- coding: utf-8 -*-


def to_encrypt(text, delta):

    result = ""

    for symbol in text:

        if symbol == " ":
            result += " "
        else:
            delta_symbol = ord(symbol)+delta

            if delta_symbol < 97:
                remainder = 97 - delta_symbol
                result += chr(123 - remainder)

            elif delta_symbol > 122:
                remainder = delta_symbol - 122
                result += chr(96 + remainder)
            else:
                result += chr(delta_symbol)

    return result


if __name__ == '__main__':
    print("Example:")
    print(to_encrypt('abc', 10))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert to_encrypt("a b c", 3) == "d e f"
    assert to_encrypt("a b c", -3) == "x y z"
    assert to_encrypt("simple text", 16) == "iycfbu junj"
    assert to_encrypt("important text", 10) == "swzybdkxd dohd"
    assert to_encrypt("state secret", -13) == "fgngr frperg"
    print("Coding complete? Click 'Check' to earn cool rewards!")
