"""
Problem statement: 
    write a program to convert Hexadecimal to binary.
    
example:
    input:7
    output:111
    
    input:10
    output:1o1o
    
"""

def hex_to_binary(hexadecimal_number):
    try:
        # Convert hexadecimal to decimal first
        decimal_number = int(str(hexadecimal_number), 16)

        # Convert decimal to binary
        binary_number = bin(decimal_number)[2:]

        return binary_number
    except ValueError:
        return "Invalid input. Please enter a valid hexadecimal number."

hex_input = input("Enter a hexadecimal number: ")

try:
    binary_output = hex_to_binary(hex_input)
    print(f"The binary representation is: {binary_output}")
except ValueError:
    print("Invalid input. Please enter a valid hexadecimal number.")
