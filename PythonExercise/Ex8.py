# June 10, 2018
# Rock , Paper, Scissors

# July 2020
import sys
import random

u=input ('Type your Choice: Rock, Sci, Paper:')
c= random.choice(['Rock','Sci','Paper'])
print('Computer Chose:',c)
if u==c:
    print('Tie')
    sys.exit()
if u=='Rock':
    if c=='Sci':
        print('User with {} wins over {}'.format(u,c))
    else:
        print('Computer with {} wins over {}'.format(u,c))
    sys.exit()
if u=='Paper':
    if c=='Rock':
        print('User with {} wins over {}'.format(u,c))
    else:
        print('{} wins over {}'.format(c,u))
    sys.exit()
if u=='Sci':
    if c=='Paper':
        print('User with {} wins over {}'.format(u,c))
    else:
        print('Computer with {} wins over {}'.format(c,u))
    sys.exit()

# June 2018

import sys

print('Please select one of the options:\n Rock=R, Paper=P, Scissors=S')
Player1 = (input('Player1:'))
player2 = (input('player2:'))

if Player1 == player2:
    print('Tie, Try again')
    sys.exit('Done')  # it is like return command inside the function ( aborts the code)

if (Player1 == 'R') and (player2 == 'S'):
    print('Player1 is the winner')
elif (Player1 == 'S') and (player2 == 'P'):
    print('Player 1 is the winner')
elif (Player1 == 'P') and (player2 == 'R'):
    print('Player 1 is the winner')
else:
    print('player 2 is the winner')
