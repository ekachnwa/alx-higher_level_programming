#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastnumber = abs(number) % 10
if number < 0:
    lastnumber = -lastnumber
    strng = "Last digit of {} is {}".format(number, lastnumber)
    if lastnumber > 5:
        print(f"{strng} and is greater than 5")
    elif lastnumber == 0:
        print(f"{strng} and is 0")
elif lastnumber < 6:
    print(f"{strng} and is less than 6 and not 0")
