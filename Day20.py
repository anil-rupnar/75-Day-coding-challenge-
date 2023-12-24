"""
Problem statement: 
    write a program to convert Binary toDecimal .
    
example:
    input:111
    output:7
    
    input:1010
    output:1o
    
"""
def binary_to_decimal(binary_str):
    decimal_num = 0
    power = 0

    # Reverse the binary string for easy calculation
    reversed_binary_str = binary_str[::-1]

    # Loop through each digit in the reversed binary string
    for digit in reversed_binary_str:
        # Convert the digit to an integer
        bit = int(digit)
        # Add the contribution of the bit to the decimal number
        decimal_num += bit * (2 ** power)
        # Move to the next power of 2
        power += 1

    return decimal_num

binary_input = input("Enter a binary number: ")

try:
    
    decimal_output = binary_to_decimal(binary_input)
    print(f"The decimal equivalent of {binary_input} is: {decimal_output}")
except ValueError:
    print("Invalid binary input. Please enter a valid binary number.")
