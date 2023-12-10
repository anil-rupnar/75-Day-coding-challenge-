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
