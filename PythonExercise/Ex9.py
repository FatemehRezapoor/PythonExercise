# June 10 , 2018
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether
#  they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very
# first exercise)
# Extras:

#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
number=random.randint(1,9)
print(number)
guess=''
i=0
while (guess!=(number) and guess!='N'):
    guess=input('Inter a number or N')
    i=i+1
    if guess=='N':
        print('Do not continue')
        break
    if int(guess)>number:
       print('You are so high')
    elif int(guess)<number:
       print('You are so low')
    else:
        print('Nice guess. You have tried %d times' % i)


