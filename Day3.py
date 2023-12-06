"""
Problem statement :
    write a program in python to find the GCD(Greatest Common Divisor) of two numbers.
    Input : two +ve integer separated by space.
    Output : +ve integer which is gcd of two numbers.

"""
def gcd(a,b):
    while b:
        a,b = b,a %b
    return a
input_numbers = input("Enter the positive integers separated by space:")
num1 , num2 = map(int,input_numbers.split())

result = gcd(num1,num2)
print(f"The GCD of {num1}and{num2}is:{result}")

"""
code Explanation :

1)Function Definition (def gcd(a, b):): This line defines a function named gcd that takes two parameters (a and b) and calculates their GCD using the Euclidean algorithm. The while loop continues until b becomes zero, and the remainder of the division is used in each iteration.

2)User Input (input("Enter two positive integers separated by space: ")): This line prompts the user to input two positive integers separated by a space. The input function returns a string.

3)String Splitting (num1, num2 = map(int, input_numbers.split())): The entered string is split into a list of substrings using the split method. The map(int, ...) converts these substrings into integers. The resulting integers are assigned to the variables num1 and num2.

4)GCD Calculation (result = gcd(num1, num2)): The gcd function is called with the two input numbers (num1 and num2) to calculate their GCD. The result is stored in the variable result.

5)Result Printing (print(f"The GCD of {num1} and {num2} is: {result}")): This line prints the GCD result, including the values of the two input numbers. The f-string syntax is used for formatting.

"""