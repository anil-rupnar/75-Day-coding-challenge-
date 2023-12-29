"""
Problem statement: 
    Given a positive n, print count of set bits in it.

    Input: 6
    Output:2
    
Explanation:
    binary represntation is '110'
    so the count of th set bit is 2.

"""
def count_set_bits(n):
    count = 0
    while n:
        # Check if the least significant bit is set (equal to 1)
        # If true, increment the count
        count += n & 1
        n >>= 1
    return count

n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    result = count_set_bits(n)
    print(f"The count of set bits in {n} is: {result}")


""" 
(base) E:\75 hard coding challenge>python ./Day25.py
Enter a positive integer: 6 
The count of set bits in 6 is: 2   

(base) E:\75 hard coding challenge>python ./Day25.py
Enter a positive integer: 20
The count of set bits in 20 is: 2  

"""