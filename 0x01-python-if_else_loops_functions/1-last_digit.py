#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = abs(number) % 10
strng = "Last digit of {} is {}".format(number, lastdigit)
if number < 0:
    lastdigit = -lastdigit
    if lastdigit > 5:
        print(f"{strng} and is greater than 5")
    elif lastdigit == 0:
        print(f"{strng} and is 0")
elif lastdigit < 6:
    print(f"{strng} and is less than 6 and not 0")
