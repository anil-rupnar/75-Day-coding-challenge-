"""
Problem statement :
    find the gretest of 3 numbers(3 numbers are not equal)
    Input : three integers separated by space denting to be compared to find greatest number.
    Output : Greatest number out of the three given numbers.
    
"""
def maximum(a, b, c):
    if (a >= b) and (a >= c):
        largest = a
    elif (b >= a) and (b >= c):
        largest = b
    else:
        largest = c
    return largest

print("Enter the numbers:")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

print("Maximum Value:", maximum(a, b, c))

"""
code Explanation:
1)from calendar import c
    This line imports the c module from the calendar library.
    However, it seems unnecessary in the context of the rest of the code, and the calendar module is not used later. You can safely remove this line.
2)import numbers
    This line imports the numbers module, but it is also unused in the provided code. You can remove it unless you plan to use it later in your program.
3)def maximum(a, b, c):
    This line defines a function named maximum that takes three parameters (a, b, and c). This function is designed to find and return the maximum of the three input values.
4)if (a >= b) and (a >= c):
        largest = a
    This line checks if a is greater than or equal to both b and c. If this condition is true, it means that a is the largest, so it assigns the value of a to the variable largest.
5)elif (b >= a) and (b >= c):
        largest = b
    This line is an "else if" condition that checks if b is greater than or equal to both a and c. If true, it assigns the value of b to the variable largest.
6)else:
        largest = c
    If none of the previous conditions are true, it means that c is the largest, so it assigns the value of c to the variable largest.
7)return largest
    The function returns the value stored in the variable largest, which represents the maximum of the three input values.
8)print("Enter the numbers:")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
These lines prompt the user to enter three numbers and convert the input values to integers using int(input()).
9)print("Maximum Value:", maximum(a, b, c))
    Finally, this line calls the maximum function with the user-input values of a, b, and c and prints the result, which is the maximum of the three numbers.
"""