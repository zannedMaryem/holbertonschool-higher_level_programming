#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) < 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:\n1: ", sys.argv[1])
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        for i in range(2, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
