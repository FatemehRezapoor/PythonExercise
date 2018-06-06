# June 5, 2018
# The commands you can use for list

# * Define a list*
OneD = ['a', 'b', 'c']
TwoD = [['a', 'b', 1], ['c', 'd', 2, 4]]

# * ELEMENTS *

print(OneD[0])  # the index starts from 0 in python
print(TwoD[0])
print(TwoD[0][1])

# * LENGTH *
print(len(OneD))
print(len(TwoD))
print(len(TwoD[1]))

# * APPEND *: Add sth to the end of list
OneD.append('1')
print(OneD)
TwoD.append(['n'])
print('From Append %s' % TwoD)
TwoD[0].append('n')
print(TwoD)

# * INSERT *: Add sth to the specific point in the list
OneD.insert(0, 'man')
print(OneD)
TwoD.insert(1, 'man')
print(TwoD)

# * EXTEND *: Extends the list according to new iteration

new = [8, 8, 9]
OneD.extend(new)
print(OneD)
TwoD.extend(new)
print(TwoD)

# * REMOVE *: Removes the first item which matches with input
OneD.remove('man')
print(OneD)

# * POP *: Removes the item from list and return it
OneD.pop(0)
print(OneD)
TwoD.pop(0)
print(TwoD)

# * CLEAR *: Remove all items from the list
new.clear()
print(new)

# * INDEX *: Returns the index of input
print(OneD.index('b'))
print(TwoD.index(8))

# * COUNT *: Counts and return number of time input is repeated
print(OneD.count(8))
print(OneD)

# * REVERSE *: Reverse the list
print(OneD.reverse())
print(OneD)

# * SORT *: Sorts the list
# print(OneD.sort())
# print(OneD)
