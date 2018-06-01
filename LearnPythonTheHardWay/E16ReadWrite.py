# June 1, 2018
from sys import argv

script, filename = argv
print('Hello. You want to open %s text file' % filename)
txt = open(filename, 'w')
print('File is opened\n next step: Deleting')
txt.truncate()
sen1 = input('Sentence 1:')
sen2 = input('Sentence 2:')
txt.write('writing in progress')
txt.write('\n')
txt.write(sen1)
txt.write('\n')
txt.write(sen2)
txt.close()
txtmine = open(filename, 'r')
print(txtmine.read())
txtmine.close()
# *What if you want to create a text file that does not excist?*
t = open('new.txt', 'w+')

# How to open a file in read and write mode?
path = 'D:/Repository/LearnPythonTheHardWay/new.txt'
txt = open(path, 'r+')
print(txt.read())
txt.write('This is a new line 5')  # If you don't truncate, It will write in the end of lines
print(txt.read())
txt.close()


