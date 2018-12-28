#!/usr/bin/python

import random

english_strings = {"English", "english", 'eng', 'Eng', 'en', 'En', 'EN', 'ENG', 'ENGLISH'}
german_strings = {"GERMAN", 'german', 'ger', 'Ger'}
print("This script can generate passphrases from 2 Languages.\n")
print("English and German\n")
option1 = input("What language would you like to use for your generation?\n")
option1 = str(option1)


def eng_gen():
    with open('english.txt') as a:
        lines1 = [line.rstrip('\n') for line in a]

    with open('delimiters.txt') as b:
        lines2 = [line.rstrip('\n') for line in b]

    with open('numbers.txt') as c:
        lines3 = [line.rstrip('\n') for line in c]

    def rndpw1():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_line2 + rnd_num + rnd_del)

    def rndpw2():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_line2 + rnd_del + rnd_num)

    def rndpw3():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_del + rnd_line2 + rnd_num)

    def rndpw4():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_del + rnd_num + rnd_line2)

    def rndpw5():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_num + rnd_line2 + rnd_del)

    def rndpw6():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_num + rnd_del + rnd_line2)

    def rndpw7():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_line + rnd_del + rnd_num)

    def rndpw8():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_line + rnd_num + rnd_del)

    def rndpw9():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_del + rnd_line + rnd_num)

    def rndpw10():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_del + rnd_num + rnd_line)

    def rndpw11():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_num + rnd_line + rnd_del)

    def rndpw12():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_num + rnd_del + rnd_line)

    def rndpw13():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_line + rnd_line2 + rnd_num)

    def rndpw14():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_line + rnd_num + rnd_line2)

    def rndpw15():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_line2 + rnd_line + rnd_num)

    def rndpw16():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_line2 + rnd_num + rnd_line)

    def rndpw17():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_num + rnd_line + rnd_line2)

    def rndpw18():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_num + rnd_line2 + rnd_line)

    def rndpw19():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_line + rnd_line2 + rnd_del)

    def rndpw20():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_line + rnd_del + rnd_line2)

    def rndpw21():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_line2 + rnd_line + rnd_del)

    def rndpw22():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_line2 + rnd_del + rnd_line)

    def rndpw23():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_del + rnd_line + rnd_line2)

    def rndpw24():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_del + rnd_line2 + rnd_line)

    listfunct = [rndpw1, rndpw2, rndpw3, rndpw4, rndpw5, rndpw6, rndpw7, rndpw8, rndpw9, rndpw10, rndpw11, rndpw12,
                 rndpw13, rndpw14, rndpw15, rndpw16, rndpw17, rndpw17, rndpw18, rndpw19, rndpw20, rndpw21, rndpw22,
                 rndpw23, rndpw24]

    def repeater():
        i = 0
        numpass = input("How many passwords would you like to create?\n")
        numpass = int(numpass)
        while i != numpass:
            i += 1
            random.choice(listfunct)()

    repeater()
    print('')


def ger_gen():
    with open('german.txt', encoding='latin_1') as a:
        lines1 = [line.rstrip('\n') for line in a]

    with open('delimiters.txt') as b:
        lines2 = [line.rstrip('\n') for line in b]

    with open('numbers.txt') as c:
        lines3 = [line.rstrip('\n') for line in c]

    def rndpw1():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_line2 + rnd_num + rnd_del)

    def rndpw2():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_line2 + rnd_del + rnd_num)

    def rndpw3():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_del + rnd_line2 + rnd_num)

    def rndpw4():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_del + rnd_num + rnd_line2)

    def rndpw5():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_num + rnd_line2 + rnd_del)

    def rndpw6():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line + rnd_num + rnd_del + rnd_line2)

    def rndpw7():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_line + rnd_del + rnd_num)

    def rndpw8():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_line + rnd_num + rnd_del)

    def rndpw9():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_del + rnd_line + rnd_num)

    def rndpw10():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_del + rnd_num + rnd_line)

    def rndpw11():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_num + rnd_line + rnd_del)

    def rndpw12():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_line2 + rnd_num + rnd_del + rnd_line)

    def rndpw13():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_line + rnd_line2 + rnd_num)

    def rndpw14():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_line + rnd_num + rnd_line2)

    def rndpw15():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_line2 + rnd_line + rnd_num)

    def rndpw16():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_line2 + rnd_num + rnd_line)

    def rndpw17():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_num + rnd_line + rnd_line2)

    def rndpw18():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_del + rnd_num + rnd_line2 + rnd_line)

    def rndpw19():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_line + rnd_line2 + rnd_del)

    def rndpw20():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_line + rnd_del + rnd_line2)

    def rndpw21():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_line2 + rnd_line + rnd_del)

    def rndpw22():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_line2 + rnd_del + rnd_line)

    def rndpw23():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_del + rnd_line + rnd_line2)

    def rndpw24():
        rnd_line = random.choice(lines1)
        rnd_line2 = random.choice(lines1)
        rnd_del = random.choice(lines2)
        rnd_num = random.choice(lines3)
        print('\n' + rnd_num + rnd_del + rnd_line2 + rnd_line)

    listfunct = [rndpw1, rndpw2, rndpw3, rndpw4, rndpw5, rndpw6, rndpw7, rndpw8, rndpw9, rndpw10, rndpw11, rndpw12,
                 rndpw13, rndpw14, rndpw15, rndpw16, rndpw17, rndpw17, rndpw18, rndpw19, rndpw20, rndpw21, rndpw22,
                 rndpw23, rndpw24]

    def repeater():
        i = 0
        numpass = input("How many passwords would you like to create?\n")
        numpass = int(numpass)
        while i != numpass:
            i += 1
            random.choice(listfunct)()

    repeater()
    print('')


if option1 in english_strings:
    eng_gen()

if option1 in german_strings:
    ger_gen()
else:
    print("You have not made a valid choice, please run this script again. Goodbye.")
exit()
