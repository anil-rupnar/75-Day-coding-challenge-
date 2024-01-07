"""
Problem statement: 
write a program to add two fractions and Display their sum in reduced form. 

Example:
Input: 1/2 3/2
output: 2/1
"""
from fractions import Fraction

def add_fractions(fraction1, fraction2):
    result = fraction1 + fraction2
    return result

def reduce_fraction(fraction):
    return Fraction(fraction).limit_denominator()

def main():
    
    input_fraction1 = input("Enter the first fraction (e.g., 1/2): ")
    input_fraction2 = input("Enter the second fraction (e.g., 3/2): ")

    try:
        # Convert input strings to Fraction objects
        fraction1 = Fraction(input_fraction1)
        fraction2 = Fraction(input_fraction2)

        # Add fractions
        sum_fraction = add_fractions(fraction1, fraction2)
        
        reduced_sum_fraction = reduce_fraction(sum_fraction)
      
        print("Sum in reduced form:", reduced_sum_fraction)

    except ValueError:
        print("Invalid input. Please enter fractions in the format 'numerator/denominator'.")

if __name__ == "__main__":
    main()


"""
Output:
(base) E:\75 hard coding challenge>python ./Day34.py
Enter the first fraction (e.g., 1/2): 1/2
Enter the second fraction (e.g., 3/2): 3/2
Sum in reduced form: 2

(base) E:\75 hard coding challenge>python ./Day34.py
Enter the first fraction (e.g., 1/2): 1/3
Enter the second fraction (e.g., 3/2): 3/9
Sum in reduced form: 2/3

(base) E:\75 hard coding challenge>


"""