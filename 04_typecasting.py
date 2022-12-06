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
