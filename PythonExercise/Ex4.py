# June 10, 2018
# Asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number. For example,
# 13 is a divisor of 26 because 26 / 13 has no remainder.)

# July 2020
l=[]
n = 5
for i in range(1,n+1):
    if n%i==0:
        l.append(i)
    else:
        continue
print(l)

# June 2018
number = int(input('Enter your number please: '))
b = []
for i in range(1, number + 1):
    if number % i == 0:
        b.append(i)

if len(b) == 2:
    print('Your number is prime with %r divisors' % b)
else:
    print('Divisors: %r' % b)
