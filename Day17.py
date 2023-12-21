"""
Problem statement: Check whether a number is a plus perfect number.
Input: An integer N.
Output: True if N is a plus perfect number, False otherwise.
"""

def is_plus_perfect(n):

    num_digits = len(str(n))  
    sum_of_powers = 0  

    for digit in str(n):
        power = int(digit) ** num_digits  
        sum_of_powers += power 

    return sum_of_powers == n  
def main():
    
    n = int(input("Enter a number: "))

    if is_plus_perfect(n):  
        print(f"{n} is a plus perfect number")
    else:
        print(f"{n} is not a plus perfect number")

if __name__ == "__main__":
    main()  
