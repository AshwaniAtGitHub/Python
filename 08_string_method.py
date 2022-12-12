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

