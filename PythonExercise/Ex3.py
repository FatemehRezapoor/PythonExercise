# June 10, 2018
# Take a list and write a program that prints out all the elements of the list that are less than input number.
number = int(input('Number:\t'))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in range(0, len(a)):
    if a[i] < number:
        b.append(a[i])
    else:
        pass

print(b)
