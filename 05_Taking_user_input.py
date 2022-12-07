'''
    syntax -> 
    variable = input()

    input function returns the value as a string. Hence, we have to typecast them whenever required to another data type.

'''
#Example->
a = input("Enter your name: ")
print("My name is", a)

x = input("Enter first number: ")
y = input("Enter second number: ")

print (x+y)

print(int(x) + int(y))