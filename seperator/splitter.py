#!/usr/bin/python3

import string


def main():
    fobj = open("test.txt")
    newStr = ""
    for line in fobj:
        newStr = line.splitlines(True)
        print(newStr)

if __name__ == "__main__":
    main()
