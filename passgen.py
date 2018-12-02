#!/usr/bin/python

import random


with open('words.txt') as a:
    lines1 = [line.rstrip('\n') for line in a]

with open('delimiters.txt') as b:
    lines2 = [line.rstrip('\n') for line in b]

with open('numbers.txt') as c:
    lines3 = [line.rstrip('\n') for line in c]


def rndpw():
    rnd_line = random.choice(lines1)
    rnd_line2 = random.choice(lines1)
    rnd_del = random.choice(lines2)
    rnd_num = random.choice(lines3)
    print('\n' + rnd_line + rnd_del + rnd_num + rnd_line2)


def repeater():
    i = 0
    numpass = input("How many passwords would you like to create?\n")
    numpass = int(numpass)
    while i != numpass:
        i += 1
        rndpw()


repeater()
