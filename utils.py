#!/usr/bin/env python3
"""
utilities when modifying the wordlists to check
whether each name in the file is unique and not
an existing program name

author: case 2021-01-30
@case0x00

"""

import sys

from namegen import read, get_programs


def main(file):
    unique = True
    for i in range(len(file)):
        if file.count(file[i]) > 1:
            print(f"'{file[i]}' AT LINE {i+1} IS NOT UNIQUE")
            unique = False
        if file[i] in get_programs():
            print(f"'{file[i]}' AT LINE {i+1} IS A PROGRAM PREFIX")
            unique = False

    if unique:
        print("ALL VALUES WERE UNIQUE")


if __name__ == "__main__":
    if len(sys.argv) > 2 or len(sys.argv) == 1:
        print("INCORRECT NUMBER OF ARGUMENTS")
        exit(-1)

    file = read(f"dictionary/{sys.argv[1]}")
    main(file)