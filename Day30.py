"""
Problem statement: 
write a program to check whether a year is a leep year or not ?
Example:
Input: 2016
output:leap year
"""

def is_leap_year(year):
    
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


year = int(input("Enter a year: "))

if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


"""
Output:

(base) E:\75 hard coding challenge>python ./Day30.py
Enter a year: 2016
2016 is a leap year.

(base) E:\75 hard coding challenge>python ./Day30.py
Enter a year: 2019
2019 is not a leap year.

(base) E:\75 hard coding challenge>

"""