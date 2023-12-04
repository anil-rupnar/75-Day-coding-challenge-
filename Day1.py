"""
Problem statement :
    factorial of a non negative integer , is multiplication of all integers smaller than or equal to n.
    for example factorial of 6 is 6*5*4*3*2*1  which is 720. 

"""
def factorial(n):
    if n==0:
        return 1
    return n * factorial(n-1)
print("Enter the num")
num = int(input())
print("factorial of ",num,"is",factorial(num))
        