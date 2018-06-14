# June 12, 2018

#  For example, say I type the string: My name is Michele
# Then I would see the string: Michele is name My shown back to me.

sen='My name is sara'
sent=sen.split(' ')

# METHOD 1
senr=list(reversed(sent))

for x in senr:
    print(x,end=' ') # Avoids the print command from printing in a new line

# METHOD 2
a=' '.join(reversed(sent))
print(a)

# JOIN IN PYTHON
# Joins a sequence of elements

s = "-";
seq = ("a", "b", "c"); # This is sequence of strings.
print (s.join( seq ))
