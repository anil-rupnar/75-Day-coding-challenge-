"""
Problem statement: 
Given two Postive Integer Num1 and Num2 ,the task is to find the reminder when Num1 is divided by 2.

Example:
Input: Num1=5 NUm2=3
output:2
"""

def get_remainder(num, divisor):
    return num - divisor * (num // divisor)


num = int(input("Enter Number: "))
divisor = int(input("Enter Divisor: "))


print("Remainder:", get_remainder(num, divisor))

"""
Output:
Anil Rupnar@DESKTOP-6UV394I MINGW64 /e/75 hard coding challenge (main)
$ python ./Day29.py 
Enter Number: 5
Enter Divisor: 3
Remainder: 2

"""