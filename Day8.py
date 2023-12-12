"""
Problem statement :
    find ot smallest of 4 numbers(numbers are not equal)
    Input : Four integer separated by space denoting the numbers to be compared to find smallest number.
    Output : Smallest number out of the four given numbers.
        
"""
print("Enter the four Numbers")
a = int(input("Enter The First Number"))
b = int(input("Enter The secand NUmber:"))
c = int(input("Enter The third NUmber:"))
d = int(input("Enter The Fourth NUmber:"))

print("smallest Number",min(a,b,c,d))