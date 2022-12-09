# String Slicing & Operations on String

name = "Ashwani Maurya"
print(name)

# length
nameLen = len(name)
print("length of name is",nameLen)

#slicing
pie = "ApplePie"
print(pie[:5])      #Slicing from Start
print(pie[5:])      #Slicing till End
print(pie[2:6])     #Slicing in between
print(pie[-8:])     #Slicing using negative index this will begin with (len(pie)-8)th index

# slicing in between name
print(name[0:7]) # slices the given string(name) from 0th to (7-1)th index.
print(name[4:9]) # slices the given string(name) from 4th to (9-1)th index.
print(name[2:6]) # slices the given string(name) from 2th to (6-1)th index.
print(name[5:10]) # slices the given string(name) from 5th to (10-1)th index.


# Loop through a String:
# Strings are arrays and arrays are iterable. Thus we can loop through strings.

# let's try to print A to Z using loop

alphabets = "ABCDEFHIJKLMNOPQRSTUVWXYZ"
for i in alphabets:
    print(i)
