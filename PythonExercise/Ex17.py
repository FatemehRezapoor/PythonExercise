# June 15, 2018

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed
# correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is
# a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses
# the correct number, the game is over.
import random

com=(random.randint(1000,9999))
print(type(str(com)))
coml= list(str(com))
print(coml)
cow=0
Bull=0
guess= False

while guess is False:
    cow=0
    Bull=0
    Userl=list(input('Your Guess:'))
    if Userl == coml:
        print('You are Correct. Your answer is {}\n Computer answer: {}'.format(Userl,coml))
        guess = True
    else:
        for i,v in enumerate(coml):
            if Userl[i]==v:
                cow=cow+1
            if Userl.count(v):
                   Bull= Bull+1
        print('Cows : {} and Bulls {}:'.format(cow,Bull))
        guess=False

# June 2018
import random

s = '123456789'
a = random.sample(''.join(s), 4)
print(a)
print(type(a))
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
