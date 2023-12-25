"""
Problem statement: 
    write a program to convert Decimal to binary.
    
example:
    input:7
    output:111
    
    input:10
    output:1o1o
    
"""
"""
Algorithm Steps:

Input:
    Accept a decimal number as input.
Initialize Variables:
    Set a variable to store the binary representation.
Conversion Process:
    Divide the decimal number by 2 and note the remainder.
    Update the decimal number with the quotient obtained from the division.
    Append the remainder to the binary representation.
Repeat:
    Repeat steps 3 until the decimal number becomes 0.
Reverse:
    The binary representation obtained in step 3 will be in reverse order. Reverse it to get the correct binary representation.
Output:
    Display the binary representation as the output.

"""
def decimal_to_binary(decimal_number):
    binary_representation = bin(decimal_number)[2:]
    return binary_representation

decimal_input = int(input("Enter a decimal number: "))

binary_output = decimal_to_binary(decimal_input)

print(f"The binary representation of {decimal_input} is: {binary_output}")

"""
Note:
    This program uses the built-in bin function in Python to convert a decimal number to its binary representation.
    The [2:] is used to slice the string and remove the '0b' prefix that bin adds to the binary representation.

"""