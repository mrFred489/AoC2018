#!/bin/bash

if [ -z "$1" ]
then
    exit 1
fi 

if [ ! -f "$1.py" ]; then
    echo "from collections import *
import itertools
import random
import sys

f = open(\"$1.txt\").read().split(\"\n\")" > "$1.py"
    git add "$1.py"

fi

emacs26 "$1.py" &

if [ ! -f "$1.txt" ]; then
    session=$(cat "session.txt")
    curl https://adventofcode.com/2018/day/$1/input --cookie "session=${session//[$'\t\r\n']}" > "$1.txt"
    git add "$1.txt"
fi

