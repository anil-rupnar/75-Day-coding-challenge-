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
