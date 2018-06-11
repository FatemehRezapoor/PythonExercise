# June 10 , 2018
# Comprehension in python ( used for list )
# tuple is similar to list. You can not change the elements in tuple

""" How to comp a list:            list=[x for x in range()]         """

# **Example 1: For loop **

word = 'shark'
listword = []
for x in word:
    listword.append(x)

print(listword)

# How to comp: variable=[x for x in iterable]
""" Out put is x which is saved in a list"""
listword = [x for x in word]
print(listword)

# ** Example 2: If and For **

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')  # tuple is similar to list but you can not change it
fish_list = []
for x in fish_tuple:
    if x != 'octopus':
        fish_list.append(x)

print(fish_list)
""" Output is x which is saved in list. After passing a condition"""
fish_list = [x for x in fish_tuple if x != 'octopus']
print(fish_list)

# Example 3: if and For

double = [x ** 2 for x in range(0, 10) if x % 2 == 0]  # output is x**2
print(double)

# Exmaple 4 ( NESTED IF)

triple = [x ** 2 for x in range(0, 20) if x % 3 == 0 if x % 5 == 0]  # nested if
print(triple)

# Example 5 ( Nested For )

my_list = []

for x in [20, 40, 60]:
    for y in [2, 4, 6]:
        my_list.append(x * y)

print(my_list)

new = [x * y for x in range(20, 60, 20) for y in range(2, 6, 2)]
print(new)

# IMPORTANT: ALWAYS START FROM INSIDE YOU CODE AND PUT IT IN THE RIGHT SIDE ( LOWER THE NEST ===> RIGHT SIDE OF COMMAND)

# Example 6:
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
newa=[]

newa=[x for x in a if x%2==0]
print(newa)