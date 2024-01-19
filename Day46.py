"""
Problem Statement :
User enters Date in DD-MM-YYYY find out number of Days in month ( for now ignore the concept of leap year.)

Examples: 
Input : Date in DD-MM-YYYY format.
Output : Number of days in the Date entered by user.

Input : 12-03-2006
Output : 31
input : 31-11-1996
output : 30

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
