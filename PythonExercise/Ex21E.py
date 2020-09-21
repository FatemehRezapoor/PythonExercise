# July 2020
#Take two lists, say for example these two:
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

a = [5, 6, 5, 20, 20, 20, 3,3]
b = [20, 5, 3, 4, 5, 6]
c=[]
for i,vi in enumerate(a):
    #print(i,vi)
    for j,vj in enumerate(b):
        #print(j,vj)
        if vi==vj:
            c.append(vi)
print(c)
cclean=[]
for k in c:
    if k not in cclean:
        cclean.append(k)
print(cclean)
