"""
Problem statement: 
    write a program to convert Binary to octal .
    
example:
    input:111
    output:7

    
"""
def binary_to_octal(binary_num):
    # Convert binary to decimal first
    decimal_num = int(binary_num, 2)

    # Convert decimal to octal
    octal_num = oct(decimal_num)

    # Extract the octal representation (excluding the '0o' prefix)
    octal_result = octal_num[2:]

    return octal_result

"""
Output:
PS D:\75 hard coding challenge> python .\Day20_1.py     
Enter a binary number: 11111
The octal representation is: 37 
PS D:\75 hard coding challenge> python .\Day20_1.py
Enter a binary number: 1010101
The octal representation is: 125

"""

binary_input = input("Enter a binary number: ")
try:
    octal_output = binary_to_octal(binary_input)
    print(f"The octal representation is: {octal_output}")
except ValueError:
    print("Invalid binary number. Please enter a valid binary number.")
