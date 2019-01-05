#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.upper()
    result = 0

    for val in re.split('\W+', text):
        Checked = False
        for i in range(len(val)):

            if i == 0:
                if val[i] in VOWELS:
                    stipedflag = True
                elif val[i] in CONSONANTS:
                    stipedflag = False
                else:
                    Checked = False
                    break
            else:

                if val[i] in VOWELS and not stipedflag:
                    Checked = True
                    stipedflag = True
                elif val[i] in CONSONANTS and stipedflag:
                    Checked = True
                    stipedflag = False
                else:
                    Checked = False
                    break

        if Checked:
            result += 1
    return result

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
