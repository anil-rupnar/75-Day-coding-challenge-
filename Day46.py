"""
Problem Statement :
The user enters the Date in DD-MM-YYYY to find out the number of Days in a month ( for now ignore the concept of leap year.)

Examples: 
Input: Date in DD-MM-YYYY format.

Output: Number of days in the Date entered by the user.

Input: 12-03-2006

Output: 31

input: 31-11-1996

output: 30

"""
def days(date_str):
    # Split the input date into day, month, and year
    day, month, year = map(int, date_str.split('-'))

    # Define the number of days in each month
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Validate the month input
    if 1 <= month <= 12:
        # Return the number of days in the specified month
        return days_in_month[month]
    else:
        return "Invalid month input"

date_input = input("Enter date in DD-MM-YYYY format: ")
result = days(date_input)

print(f"Number of days in the entered month: {result}")


"""
Output :
(base) E:\75 hard coding challenge>python ./Day46.py
Enter date in DD-MM-YYYY format: 17-03-2003
Number of days in the entered month: 31

(base) E:\75 hard coding challenge>python ./Day46.py
Enter date in DD-MM-YYYY format: 19-04-2004
Number of days in the entered month: 30

"""