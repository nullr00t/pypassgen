#!/usr/bin/python

import random

with open('words.txt') as f:
    lines1 = [line.rstrip('\n') for line in f]

with open('delimiters.txt') as d:
    lines2 = [line.rstrip('\n') for line in d]

with open('numbers.txt') as n:
    lines3 = [line.rstrip('\n') for line in n]

rnd_line = random.choice(lines1)
rnd_line2 = random.choice(lines1)
rnd_del = random.choice(lines2)
rnd_num = random.choice(lines3)

print('\n' + rnd_line + rnd_del + rnd_num + rnd_line2)

