#!/usr/bin/env python3
"""
generates codenames for projects

args:
    BATCH: batch size (default 1)
    PROG: program to execute (default random)

author: case 2021-04-24
@caserobotics

"""

from random import *
import sys
import os

def read(file):
    with open(file) as f:
        lines = [line.strip("\n") for line in f]
    return lines

current_dir = os.path.dirname(os.path.realpath(__file__))


PREFIX = read(f"{current_dir}/dictionary/prefix")
SUFFIX = read(f"{current_dir}/dictionary/suffix")
EXISTING_PROJ = read(f"{current_dir}/dictionary/existing_proj")

def get_programs():
    """
    reserved program prefixes
    """
    return ["ULTRA", "OLYMPUS", "MAGIC"]

def is_unique(item, itemlist):
    return bool(item not in itemlist)
    
def gen_part(word):
    if word == "suffix":
        return SUFFIX[randint(0,len(SUFFIX)-1)]
    elif word == "prefix":
        return PREFIX[randint(0,len(PREFIX)-1)]

def main(program, batch):
    codenames = []

    if program == "random":
        while (len(codenames) < batch):
            codename = gen_part("prefix") + gen_part("suffix")
            if is_unique(codename, EXISTING_PROJ) and is_unique(codename, codenames):
                codenames.append(codename)

    else:
        while (len(codenames) < batch):
            codename = program + gen_part("suffix")
            if is_unique(codename, EXISTING_PROJ) and is_unique(codename, codenames):
                codenames.append(codename)

    for cd in codenames:
        print(cd)


if __name__ == "__main__":
    if len(sys.argv) == 1:
        # set default args as none are supplied
        BATCH = 1
        PROG = "random"
        x = f"SELECTED 'RANDOM NAME' PROGRAM WITH BATCH SIZE 1" 
        print(x)
    elif len(sys.argv) < 4:
        # set either 1 or 2 args
        BATCH = int(sys.argv[1])

        if len(sys.argv) == 2:
            # only batch is set
            PROG = "random"
            x = f"SELECTED 'RANDOM NAME' PROGRAM WITH BATCH SIZE {BATCH}"
            print(x)

        else:
            # batch and prog are set
            PROG = str(sys.argv[2]).upper()
            if PROG not in get_programs():
                print(f"SELECTED PROG '{PROG}' IS NOT VALID")
                exit(-1)

            x = f"SELECTED {PROG} PROGRAM WITH BATCH SIZE {BATCH}"
            print(x)
        
    else:
        print("TOO MANY ARGUMENTS SUPPLIED")
        exit(-1)

    print("_"*len(x)+"\n")
    main(PROG, BATCH)
