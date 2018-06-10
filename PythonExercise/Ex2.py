# June 10, 2018
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the
# user. Hint: how does an even / odd number react differently when divided by 2?
# Extras:
#If the number is a multiple of 4, print out a different message.
number=int(input('Please inter your number:\t'))
if number%2==0:
    print('Your number is even')
    if number%4==0:
        print('This number is 4 multiple')
else:
    print('Your number is odd')
