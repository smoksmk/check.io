#!/usr/bin/python3
# -*- coding: utf-8 -*-

def sun_angle(time):
    #replace this for solution
    result = "I don't see the sun!"

    time = time.split(":")
    minutes = int(time[0]) * 60 + int(time[1]) - 360

    if minutes >= 0 and minutes <= 720:

        result = minutes / 4.0

    return result

if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    assert sun_angle("12:15") == 93.75
    print("Coding complete? Click 'Check' to earn cool rewards!")
