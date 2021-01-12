"""
utilities when modifying the wordlists to check
whether each name in the file is unique and not
an existing program name
"""

import sys
from collections import Counter

from namegen import read, get_programs


FILE = read(f"dictionary/{sys.argv[1]}")

def main():
    unique = True
    for i in range(len(FILE)):
        if FILE.count(FILE[i]) > 1:
            print(f"'{FILE[i]}' AT LINE {i+1} IS NOT UNIQUE")
            unique = False
        if FILE[i] in get_programs():
            print(f"'{FILE[i]}' AT LINE {i+1} IS A PROGRAM PREFIX")
            unique = False

    if unique:
        print("ALL VALUES WERE UNIQUE")


if __name__ == "__main__":
    if len(sys.argv) > 2:
        print("INCORRECT NUMBER OF ARGUMENTS")
        exit(-1)
    main()