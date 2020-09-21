# June 10, 2018
# Take a list and write a program that prints out all the elements of the list that are less than input number.

# July 2020
sn=input('Inter the numbers: ')
n=input('Inter comparison value:')
l=sn.split()
print(type(sn.split()))
for i in l:
    if int(i)>5:
        print(i)
    else:
        print('{} is smaller or equal to {}'.format(i,n))

# June 10
number = int(input('Number:\t'))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in range(0, len(a)):
    if a[i] < number:
        b.append(a[i])
    else:
        pass

print(b)

# How to the above with a function
def compare(a,number):
    b=[]
    for i in range(0, len(a)):
        if a[i] < number:
            b.append(a[i])
        else:
            pass

    print(b)

compare(a,number)
