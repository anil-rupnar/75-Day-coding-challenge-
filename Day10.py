"""
Problem statement :
    User Enter Date in DD-MM-YYYY find out number of days in month(Now ingnore The concept of leap year ).
    Input : Date in DD-MM-YYYY format.
    Output : Number of days in the Date entered by user.
        
"""
def days_in_month(date):
    day, month, year = map(int, date.split('-'))
    days_in_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    return f"The number of days in {date} is: {days_in_month[month]}" if month in days_in_month else "Invalid month entered. Please enter a valid month (1-12)."

user_date = input("Enter the date in DD-MM-YYYY format: ")
print(days_in_month(user_date))
