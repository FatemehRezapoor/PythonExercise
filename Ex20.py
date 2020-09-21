# June 15, 2018

# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.
# At the end of this exchange, your program should print out how many guesses it took to get your number.
# July 2020
import random

def myguess(uinput):
    #uinput= 12
    cinput=random.randint(0,100)
    print('Com initial guess is : {}'.format(cinput))
    minv = 0
    maxv = 100
    while uinput!=cinput:
        if cinput>uinput:
            maxv = cinput
            cinput=round((abs((cinput-minv))/2)+minv)
        elif cinput<uinput:
            minv=cinput
            cinput=round(((abs(maxv-cinput))/2)+cinput)
    return cinput

if __name__ == '__main__':
    print('Your guess is {}'.format(myguess(24)))

# June 2018

usernum = int(input('Please enter your number here:'))
maxn = 100
minn=0
guess = (maxn+minn)/ 2
guide=''
while guide!='T':
    guide = input('computer guess: %d- Is computer guess H(higher),L(Lower), T(True):' % guess)
    if guide=='H':
        maxn=guess
        guess=(maxn+minn)//2
    elif guide=='L':
        minn=guess
        guess=(minn+maxn)//2
    elif guide=='T':
        break
print('Your number is %d' %guess)

