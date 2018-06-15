# June 15, 2018
# Write a password generator in Python.
# random module can be sued to generate random list from your own inputs

import random

weak = '123456789abcdefghijklmnopqrstuvwxyz'
strong = '123456789abcdefghijklmnopqrstuvwxyz@#$%^&*'
password = input('W (weak) or S (strong)')
if password == 'W':
    passweak = random.sample(''.join(weak), 4)
    for x in passweak:
        print(x, end=''),
else:
    passtrong = random.sample(''.join(strong), 8)
    for x in passtrong:
        print(x, end=''),
