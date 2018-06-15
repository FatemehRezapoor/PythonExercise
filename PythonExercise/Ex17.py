# June 15, 2018

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is
# a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over.

import random

s = '123456789'
a = random.sample(''.join(s), 4)
print(a)
guess = ''
while guess != a:
    c1 = 0
    c2 = 0
    guess = list(input('Your guess is:'))
    for i in range(0, len(guess)):
        if guess[i] == a[i]:
            c1 = c1 + 1
            # print('C1=%d'%c1)
        elif guess[i] in a:
            c2 = c2 + 1
            # print('C2=%d'%c2)
    print('%d: Cow _ %d: Bull' % (c1, c2))
print('Well done. Final number is: %r' % a)
