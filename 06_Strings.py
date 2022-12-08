'''
What are strings?
In python, anything that you enclose between single or double quotation marks is considered a string. A string is essentially a sequence or array of textual data. Strings are used when working with Unicode characters.
'''

#Example
name = "Ashwani"
print("Hello, " + name)

#Strings are like an array of character
#Example
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])


#Multiline Strings

message = ''' Python's convenience has made it the most popular language for machine learning and artificial intelligence.
Python's flexibility has allowed Anyscale to make ML/AI scalable from laptops to clusters.'''

print(message)


#Looping through the string

color = "White"
for i in color:
    print(i)