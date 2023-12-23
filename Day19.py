"""
Problem statement: 
    write a program to convert Decimal to binary.
    
example:
    input:7
    output:111
    
    input:10
    output:1o1o
    
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