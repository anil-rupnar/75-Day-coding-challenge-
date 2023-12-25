"""
Problem statement: 
    write a program to convert Binary to hexadecimal .
    
example:
    input:111
    output:7
 
"""
def binary_to_hexadecimal(binary_num):
    # Convert binary to decimal first
    decimal_num = int(binary_num, 2)

    # Convert decimal to hexadecimal
    hexadecimal_num = hex(decimal_num)

    # Extract the hexadecimal representation (excluding the '0x' prefix)
    hexadecimal_result = hexadecimal_num[2:]

    return hexadecimal_result

binary_input = input("Enter a binary number: ")
try:
    hexadecimal_output = binary_to_hexadecimal(binary_input)
    print(f"The hexadecimal representation is: {hexadecimal_output}")
except ValueError:
    print("Invalid binary number. Please enter a valid binary number.")


""" 
Output:
PS D:\75 hard coding challenge> python .\Day20_2.py
Enter a binary number: 1010101
The hexadecimal representation is: 55
PS D:\75 hard coding challenge> python .\Day20_2.py
Enter a binary number: 1111111
The hexadecimal representation is: 7f
PS D:\75 hard coding challenge>   


"""