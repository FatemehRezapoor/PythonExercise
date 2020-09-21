# June 10, 2018
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
#If the number is a multiple of 4, print out a different message.

# Date: July 13, 2020
num = input('Type your number:')
if int(num)%2 is 0:
    print(' Number {} is even'.format(num))
    if int(num)%4==0:
        print('Number {} is a multiple of 4'.format(num))
else:
    print('Number {} is odd'.format(num))

# Date: June 10, 2020
number=int(input('Please inter your number:\t'))
if number%2==0:
    print('Your number is even')
    if number%4==0:
        print('This number is 4 multiple')
else:
    print('Your number is odd')
