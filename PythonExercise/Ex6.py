# June 10, 2018
# Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that
# reads the same forwards and backwards.)

# Method 1 ( Using list )
a = input('word: \t')
b = []
c = []
for i in a:
    b.append(i)

print(b)
c = list(reversed(b))  # Didn't use list.reverse becasue it doesn't give
print(c)
if b == c:
    print('M1:These are identical')
else:
    print('M1:Not the same')

# Method 2 ( use string )
arev = a[::-1]  # This is called extended slice notation ([begin:end:step])
print(arev)
if a == arev:
    print('M2:They are identical')
else:
    print('M2:Not the same')

# Method 3 ( make reverse function)
x = ''

# print(len(a))
def reverse(a):
    for i in range(0, len(a)):
        x = x + a[len(a) - 1 - i]  # or you can write: x+=... ( a+=b means a=a+b)
    print(x)


# Note: example of extended slice syntax
l = list(range(0, 10))
print(l[::2])
