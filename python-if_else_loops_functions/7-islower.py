#!/usr/bin/python3
def islower(c):
    for i in range(ord('a'), ord('z')):
        if ord(c) == i:
            return(True)
        else:
            return(False)