"""
Problem statement: 
    Given a positive integer N, find the factorial of N.

    Input: 5
    Output:10
    
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


input_number = int(input("Enter a number to find Factorial :"))
output_factorial = factorial(input_number)
print(output_factorial)
