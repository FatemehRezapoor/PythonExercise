# July 2020
# Make XO game
"""
1. Reading the horizental and vertical and diagonal data in the list
2. Check to see if the elements equal. If they do, there is a winner. If they don't there is no winner.
3. The different methods to program these steps are saved in the bottom of the document
"""
play = [[21, 22, 2,115],
        [15, 36, 15,5],
        [90, 15, 1,5],
        [15, 36, 1,5]]
emp=[]

# Step 1+2: READING + LOOKING FOR WINNER

def listtoset(emp):
    temp=set(emp)
    if len(temp) == 1:
        for item in temp:
            print('Player {} is the winner!'.format(' '.join(str(item))))
        exit()

# READ ROWS: HORIZENTAL CHECK
for i in range(0,(len(play))):
    for j in range(0,(len(play))):
        emp.append(play[i][j])
    #print(emp)
    (listtoset(emp))
    emp=[]
#print('Done')

# READ COLUMN: VERTICAL CHECK
for j in range(0,(len(play))):
    for i in range(0,(len(play))):
        emp.append(play[i][j])
    #print(emp)
    (listtoset(emp))
    emp = []
#print('Done')

# READ DIAGONAL: LEFT TO RIGHT
for i in range(0,(len(play))):
    j=i
    emp.append(play[i][j])
(listtoset(emp))
emp = []

# READ DIAGONAL: RIGHT TO LEFT
for i in range(0,(len(play))):
    j=(len(play)-1)-i
    emp.append(play[i][j])
(listtoset(emp))

print('There is Tie!!')


























""" STEP 1: READ DATA """
#pl=len(play)
#emp=[]
# READ ROWS: HORIZENTAL CHECK
"""
for i in range(0,(len(play))):
    for j in range(0,(len(play))):
        emp.append(play[i][j])
    #print(emp)
    emp=[]
    """
# READ COLUMNS: VERTICAL CHECK
"""
for j in range(0,(len(play))):
    for i in range(0,(len(play))):
        emp.append(play[i][j])
    #print(emp)
    emp=[]
"""
# READ DIAGONAL: LEFT TO RIGHT
"""
for i in range(0,(len(play))):
    j=i
    emp.append(play[i][j])
print(emp)
emp = []
"""
# READ DIAGONAL: RIGHT TO LEFT
"""
for i in range(0,(len(play))):
    j=(len(play)-1)-i
    emp.append(play[i][j])

print(emp)
"""

""" STEP 2: CHECK FOR DUPLICATES """

#     ***METHOD 1 : FIND DUPLICATES: FOR LOOP AND LIST***

"""
#print(play[0])
#print(play[1])
t=[play[0][0]]
for item in range(1,len(play[0])):
    print(play[0][item])
    if play[0][item] not in t: # Compares elements with the base list
        t.append(play[0][item])
        print(t)
if len(t)==3 or len(t)==2:
    print('No winner')
elif len(t)==1:
    print('Player {} is the winner'.format(t[0]))
"""

#    ***METHOD 2: USE SET TO REMOVE DUPLICATES*** 

"""
tset=set(play[0])
print(tset)
if len(tset)==1:
    for item in tset:
        print('Player {} is the winner!'.format(' '.join(str(item)))) # Used for loop to remove {} when printing the results
    """

#    ***METHOD 3: USE ALL FUNCTION: IT LOOKS FOR BOOLEAN**

"""
tlis=play[0]
print(all(item == tlis[0] for item in tlis))
# METHOD 3: SIMPLE PRESENTATION of ALL Funciton:
c=[]
for item in tlis:
    c.append(item==tlis[0])
print(c)
print(all(c))
"""

