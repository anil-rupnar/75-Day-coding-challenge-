"""
Problem statement :
    find ot smallest of 4 numbers(numbers are not equal)
    Input : Four integer separated by space denoting the numbers to be compared to find smallest number.
    Output : Smallest number out of the four given numbers.
        
"""
print("Enter the four Numbers")
a, b, c, d = map(int, input("Enter the numbers separated by space: ").split())
print("Smallest number:", min(a, b, c, d))