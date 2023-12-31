"""
Problem statement: 
    write a function to return the position of the first 1 from right to left, in a binary representation of an integer.
    
    Input: 18 binary representation 010010
    Output:2
    
"""
def find_position(n):
    binary_representation = bin(n)[2:]  
    reversed_binary = binary_representation[::-1]  
    position_of_first_one = reversed_binary.find('1') + 1  

    return position_of_first_one

input_number = int(input("Enter an integer: "))
result = find_position(input_number)
print(f"{input_number} binary representation {bin(input_number)[2:]}")
print(result)

"""
E:\75 hard coding challenge>python ./Day28.py
Enter an integer: 18
18 binary representation 10010
2

E:\75 hard coding challenge>python ./Day28.py
Enter an integer: 5

"""
