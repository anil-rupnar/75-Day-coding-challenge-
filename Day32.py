"""
Problem statement: 
write a program to find GCD of two numbers.

Example:
Input: 20 28
output: 4
"""

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

num1, num2 = map(int, input("Enter two numbers separated by space: ").split())

gcd_result = find_gcd(num1, num2)
print("GCD of", num1, "and", num2, "is:", gcd_result)



"""
Output:
(base) E:\75 hard coding challenge>python ./Day32.py
Enter two numbers separated by space: 20 28
GCD of 20 and 28 is: 4

(base) E:\75 hard coding challenge>python ./Day32.py
Enter two numbers separated by space: 98 56
GCD of 98 and 56 is: 14

(base) E:\75 hard coding challenge>
"""