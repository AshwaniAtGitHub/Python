# strings are immutable.
a = "!!Ashwani!!!"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))
print(a.replace("Ashwani","Sunny"))

b="My name is Ashwani"
print(b.split(" ")) #converts string into list

heading = "welcome to python"
print(heading.capitalize())

note = "Welcome to the World. This World is amazing."
print(note.center(50))
print(len(note))
print(len(note.center(50)))

print(note.count("World"))
print(heading.endswith("python"))
print(heading.endswith("to",4,10))
print(heading.find("to")) #returns first occurance of string.
print(heading.find("toy")) #returns -1 if string not found.

print(heading.isalnum()) #returns True if the string is alfanumeric else False.

heading2 = "welcomeTo21stStreet"
print(heading2.isalnum()) #returns True if the string is alfanumeric else False.

str1 = "Welcome"
print(str1.isalpha()) #returns True only if the entire string only consists of A-Z, a-z.

str1 = "hello world"
print(str1.islower()) #returns True if all the characters in the string are lower case, else it returns False.

str1 = "WORLD HEALTH ORGANIZATION" 
print(str1.isupper()) #  returns True if all the characters in the string are upper case, else it returns False.

str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable()) #returns True if all the values within the given string are printable, if not, then return False.

str1 = "         "       #using Spacebar
print(str1.isspace()) # OUTPUT True

str2 = "  "       #using Tab
print(str2.isspace()) # OUTPUT True


str1 = "World Health Organization" 
print(str1.istitle()) # returns True only if the first letter of each word of the string is capitalized, else it returns False.

str2 = "To kill a Mocking bird"
print(str2.istitle()) # returns True only if the first letter of each word of the string is capitalized, else it returns False.

str1 = "Python is an Interpreted Language" 
print(str1.startswith("Python")) # checks if the string starts with a given value. If yes then return True, else return False.

str1 = "Python is an Interpreted Language" 
print(str1.swapcase()) # changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

str1 = "His name is Dan. Dan is an honest man."
print(str1.title()) # capitalizes each letter of the word within the string.