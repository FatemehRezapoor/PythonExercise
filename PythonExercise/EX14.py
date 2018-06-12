# June 12, 2018

# Set example: It is like list but without duplicate

name=set()
name.add('sara')
name.add('omid')
name.add('maman')
name.add('sara')

print(name)

namel=['sara','omid','maman','sara']
print(set(namel))

# How to keep the list order after using set

print(sorted(set(namel),key=namel.index))