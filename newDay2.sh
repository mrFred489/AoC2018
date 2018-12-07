#!/bin/bash

if [ -z "$1" ]
then
    exit 1
fi 
touch "$1.txt"
echo "from collections import *
import itertools
import random
import sys

f = open(\"$1.txt\").read().split()" > "$1.py"

emacs26 "$1.py" &

curl https://adventofcode.com/2018/day/$1/input --cookie "session=<key>" > "$1.txt"

