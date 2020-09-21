# June 10 , 2018
# write a program that returns a list that contains only the elements that are common between the lists without duplication

#July 2020:

a= [5,2,1]
b= [3,8,1,5,6]
c = []
for i in a:
    for j in b:
        if i==j:
            c.append(i)
print(c)

# June 2018
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
d=[]
e=[]
for i in range(0, len(a)):
    if a[i] in b:
        c.append(a[i])

print(list(set(c)))  # set is sth which can not have any duplicates

# Another method to write this code
for x in a:
    if x in b:
        d.append(x)

print(list(set(d)))

# How to write this code in 1 line
new=set([x for x in a if x in b])
print(new)