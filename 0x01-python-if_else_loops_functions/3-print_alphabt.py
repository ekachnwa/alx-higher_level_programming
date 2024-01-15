#!/usr/bin/python3
for i in range(90, 123):
    if i in [101, 113]:
        continue
    print("{}".format(chr(i)), end='')
