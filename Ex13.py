# June 12, 2016
# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.

#Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous
#two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …

# July 2020

def Fib(num):
    b=[1]
    if num==1:
        return b
    elif num==2:
        b=[1,1]
        return b
    else:
        b = [1, 1]
        for i in range(2,num):
                b.append((b[len(b)-1])+(b[len(b)-2]))
        return b

print(Fib(9))

# July 2018
def fibo(num):
    a=[1,1]
    if num==1:
        return(a[0])
    elif num==2:
        return(a)
    else:
        for x in range(2,num):
            a.append(a[x-1]+a[x-2])
        return(a)

print(fibo(8))
