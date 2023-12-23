"""
Problem statement: 
    write a program to convert Ocatal to binary.
    
example:
    input:7
    output:111
    
    input:10
    output:1o1o
    
"""
def octal_to_binary(octal_number):
    try:
        # Convert octal to decimal first
        decimal_number = int(str(octal_number), 8)
        
        # Convert decimal to binary
        binary_number = bin(decimal_number)[2:]
        
        return binary_number
    except ValueError:
        return "Invalid input. Please enter a valid octal number."

octal_input = input("Enter an octal number: ")

try:
    octal_input = int(octal_input)
    binary_output = octal_to_binary(octal_input)
    print(f"The binary representation is: {binary_output}")
except ValueError:
    print("Invalid input. Please enter a valid octal number.")
