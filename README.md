# namegen.py

generates names for my various projects using a python script. I might build it into a js script to be used for my website at some point.

## usage

set up a virtualenv and install argparse, then

```bash
# for generating 3 random codenames
$ python3 namegen.py.py -b 3
# for generating 1 ULTRA-prefixed project names
$ python3 namegen.py.py -p ULTRA
# for generating 10 MAGIC-prefixed project names
$ python3 namegen.py.py -p MAGIC -b 10
```



## to do

* figure out how to generate fish related codenames, either just using a list of vetted names or an API
* add an exclusion list for used names so they aren't used again
* web interface?