# June 15, 2018
# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.


mylist=list(input('Your ordered number:'))
num=int(input('Your number is: '))
if str(num) in mylist:
    print('This number is in the list')
else:
    for i in range(0,len(mylist)):
        if num<int(mylist[i]):
            mylist.insert(i,str(num))
            break
        else:
            mylist.insert(len(mylist),str(num))
            break

print(mylist)
