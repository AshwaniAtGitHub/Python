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

