"""
Problem statement: 
    Given two number M and N. the task to is to find the position of right most different bit in binary representation of numbers.
        
    Input: Two space separated integers M and N.
    Output: print the postion of rightmost different bit in binary representain of numbers.

constraints:
1<=M<=103
1<=n<=103
M and N takes Different values.

Example:
Input: 11 9
output:2
"""


def find_position(m, n):
    
    xor_result = m ^ n

    position = 1
    while xor_result:
        if xor_result & 1:
            return position
        xor_result >>= 1
        position += 1

    return -1


if __name__ == "__main__":
    m, n = map(int, input("Enter two integers M and N: ").split())
    

    result = find_position(m, n)
    print("Output:", result)
