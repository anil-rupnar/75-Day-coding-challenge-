"""
Problem statement: 
    write a program find N th fibonacci Number the fibonacci numbers are the numbers in the following integer sequence.

    input:9
    output:21
    
    input:12
    output:89
    
"""
def find_nth_fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b


user_input = int(input("Enter a positive integer to find its Fibonacci number: "))

result = find_nth_fibonacci(user_input)
print(f"The {user_input}th Fibonacci number is: {result}")


""" 
PS D:\75 hard coding challenge> python .\Day21.py
Enter a positive integer to find its Fibonacci number: 4
The 4th Fibonacci number is: 2  
PS D:\75 hard coding challenge> python .\Day21.py
Enter a positive integer to find its Fibonacci number: 9
The 9th Fibonacci number is: 21 

"""