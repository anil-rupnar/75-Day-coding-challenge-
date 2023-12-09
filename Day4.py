"""
Problem statement :
    write a program in python to find if number is prime or not if number is prime and print square root of number up to two decimal point precision.
    Input : a +ve integer i.
    Output : square root of number(if number is prime) or number is not prime.             

"""
import math

def isprime(n, i):
    if n == 0 or n == 1:
        return False
    if n == i:
        return True
    if n % i == 0:
        return False
    i += 1
    return isprime(n, i)

num = int(input("Enter the number to be checked: "))

if isprime(num, 2):
    print(num, "is a prime number.")
    print("Square root is %.2f" % math.sqrt(num))
else:
    print(num, "is not a prime number.")

"""
1)imports the math module, which provides mathematical functions, including the square root function (math.sqrt).
2)def isprime(n, i):
    if n == 0 or n == 1:
        return False
This defines a recursive function isprime that takes two parameters n and i. The function checks if n is equal to 0 or 1 and returns False in those cases, as 0 and 1 are not prime numbers.
3)    if n == i:
        return True
If n is equal to i, the function returns True. This is the base case for the recursion, indicating that the number is prime.
4)    if n % i == 0:
        return False
If n is divisible evenly by i, the function returns False, indicating that the number is not prime.
5)    i += 1
    return isprime(n, i)
If none of the above conditions are met, i is incremented by 1, and the function calls itself recursively with the updated values of n and i.
6)num = int(input("Enter the number to be checked: "))
    This line prompts the user to enter a number and converts the input to an integer.
7)if isprime(num, 2):
    print(num, "is a prime number.")
    print("Square root is %.2f" % math.sqrt(num))
else:
    print(num, "is not a prime number.")
the program checks if the entered number (num) is prime by calling the isprime function. If it's prime, 
it prints a message indicating that the number is prime and also prints the square root of the number with two decimal points precision. If the number is not prime, it prints a message indicating that the number is not prime. The % .2f is used for formatting the square root value to two decimal places.
"""
