# June 12, 2018
# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the
# first and last elements of the given list. For practice, write this code inside a function.

# METHOD 1

def newlist1(a):
    """ Your list format [ , , , ]"""
    b=[]
    b.append(a[0])
    b.append(a[len(a)-1])
    print(b)
my=[1,2,34,5]

# METHOD 2

def newlist2(a):
    return [a[0],a[len(a)-1]]

newlist1(my)
print(newlist2(my))