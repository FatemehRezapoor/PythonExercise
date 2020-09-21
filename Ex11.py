# July 11, 2018

# Build a function to see if a number is prime or not

# July 2020

def myprime(a):
    a=int(a)
    for i in range(2,a,1):
        if a%i==0:
            print('This is not a prime number. Divided by {}'.format(i))
            break
        elif i==a-1:
            print('This is a prime number')
myprime(15)

# July 11, 2018
def prim(number):
    import math
    if number < 10:
        a = 2
        while number % a != 0 and a < number:
            # print(a)
            a = a + 1
        if a == number:
            print('This is a prime number')
        else:
            print('Not a prime number. Divided to %r' % (a))
    else:
        b = 2
        while number % b != 0 and b < number / 2:
            # print(b)
            b = b + 1
        if b == math.ceil(number / 2):
            print('This is a prime number')
        else:
            print('Not a prime number. divided to %r' % (b))

prim(529)
