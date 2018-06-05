# June 5, 2018
# E 29 - what if

cat = input('Inter the number of cats:')
dog = input('Inter the number of dogs:')

if cat < dog:
    print('Number of cat is smaller than dog')

if cat > dog:
    print('Number of cats is larger than dog')

if cat == dog:
    print('They are equal')

# You can use Boolean inside if command

if 5>2 and 5>4:
    print('If is working')

# ** Let's compress the commands **

if cat>dog:
    print('More cat than dog')
elif cat<dog:
    print('Less cat than dog')
else:
    print('I think they are equal')
# you can have multiplr if and else in one command

if 0<int(cat)<5:
    if 0<int(dog)<5:
        print('There are at least 5 cats and dogs in the room')
    elif 6<int(dog)<8:
        print('There are a lot of dogs in the room')
else:
    print('A lot of cats')




