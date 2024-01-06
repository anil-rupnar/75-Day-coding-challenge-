"""
Problem statement: 
write a program find LCM of two Numbers.

Example:
Input: 15 20
output: 60
"""

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x, y):
    return (x * y) // gcd(x, y)


num1, num2 = map(int, input("Enter two numbers separated by space: ").split())


result = lcm(num1, num2)
print("LCM of {} and {} is: {}".format(num1, num2, result))

"""
Output:
(base) E:\75 hard coding challenge>python ./Day33.py
Enter two numbers separated by space: 15 20
LCM of 15 and 20 is: 60

(base) E:\75 hard coding challenge>python ./Day33.py
Enter two numbers separated by space: 30 60
LCM of 30 and 60 is: 60

(base) E:\75 hard coding challenge>
"""