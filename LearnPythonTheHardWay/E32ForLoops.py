# June 5, 2018
# For loop and interation
# List: container of things that are organized in order

# Let's define a For Loop ( iterable is defined by range function)

# Method1: ITERABLE: RANGE
x = 1
for x in range(0, 2):  # the range function always defines variable from the first to the last ( not includes the last)
    print('X value is %d from range interation' % (x + 1))

# There are more options to create the iterable in a for loop

# Methd 2: ITERABLE: STRING
string = 'Hi sara'
for x in string:
    print('X value is %s from string iteration', x)

# Method 3: ITERABLE: LIST
eye = ['brown', 'blue', 'green']
hair = ['blond', 'red', 'brown']
weight = [1, 2, 3, 4]

for x in eye:
    print('x value from the list: %s'% x)

# Method 4: ITERABLE: LIST IN A LIST
eyehair = [eye, hair]
for x in eyehair:
    print('x value from 2d list %s'%x)

