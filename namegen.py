"""
generates names for projects
"""

import argparse
from random import *

def read(file):
    with open(file) as f:
        lines = [line.strip("\n") for line in f]
    return lines

PREFIX = read("dictionary/prefix")
SUFFIX = read("dictionary/suffix")

def get_programs():
    return ["ULTRA", "PHANTOM", "LOTUS", "AZURE", "OLYMPUS", "MAGIC"]

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
            if is_unique(codename, codenames):
                codenames.append(codename)

    else:
        while (len(codenames) < batch):
            codename = program + gen_part("suffix")
            if is_unique(codename,codenames):
                codenames.append(codename)

    for cd in codenames:
        print(f"{cd}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--program","-p", help="program to execute")
    parser.add_argument("--batch","-b", help="batch size", default=1)

    args = parser.parse_args()

    batch = int(args.batch)

    if not args.program:
        print(f"SELECTED 'RANDOM NAME' PROGRAM WITH BATCH SIZE {batch}")
        program = "random"
    else:
        if args.program not in get_programs():
            print("SELECTED PROGRAM DOES NOT EXIST")
            exit(-1)
        else:
            program = args.program
            print(f"SELECTED '{program}' PROGRAM WITH BATCH SIZE {batch}")

    main(program, batch)