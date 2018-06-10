# June 9, 2018
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that
# tells them the year that they will turn 100 years old.
# Ask for a number and then publish the message according to the number

import datetime
today=datetime.datetime.now()
print(today.year, today.month)
name=input('What is your name?\t')
age=input('How old are you?\t')
message=('%s you will be 100 years old in %d year' %(name,((100-int(age))+today.year)))
number=int(input('Give me a number\t'))
print('\n'.join([message]*number)) # used to seperate the strings
