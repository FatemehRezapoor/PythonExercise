# June 6 , 2018
# While loop

i=0
number=[]

while i<6:
    print('i is equal to %d:' %i)
    number.append(i)
    i=i+1
    print(number)
print('Done')

numbers=[]

for i in range(0,6,2):  # To give different step to the for loop ( Here it is +2 step)
    print('This is the i from for loop: %d'%i)
    numbers.append(i)
    print(numbers)