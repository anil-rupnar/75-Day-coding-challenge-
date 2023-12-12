"""
Problem statement :
    find the gretest of 3 numbers(3 numbers are not equal)
    Input : three integers separated by space denting to be compared to find greatest number.
    Output : Greatest number out of the three given numbers.
    
"""
def find_maximum(a, b, c):
    return max(a, b, c)

print("Enter three numbers separated by space:")
a, b, c = map(int, input().split())

maximum_value = find_maximum(a, b, c)
print("Greatest number:", maximum_value)

