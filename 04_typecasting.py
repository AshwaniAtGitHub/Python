'''
    Types of Typecasting
    1. Explicit conversion
    2. Implicit conversion

    1. Explicit conversion

    The conversion of one data type into another data type, done via developer's or progammer's intervention or manually as per the requirement, is known as explicit type conversion.

    It can be achieved with the help of Python's build-in type conversion functions such as int(), float(), hex(), oct(), str(), etc.

'''

string = "15"
number = 7
string_number = int(string) #throws an error if the string is not a valid integer
sum= number + string_number
print("The Sum of both the numbers is: ", sum)


'''
    2. Implicit conversion
    Data types in pyhton do not have the same level that is ordering of data type is not the same in Python.
    Some of the data types have higher order and some have lower order. While performing any operations on variables with different data types in Python, one of the variable's data types will be changed to the higher data type.
    According to the level, one data types will be converted into another by the Python interpreter itself. This is called, implicit typecasting in python.

    Python converts a smaller data type to a higher data type to prevent data loss.

'''

# Python automatically converts
# a to int
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))