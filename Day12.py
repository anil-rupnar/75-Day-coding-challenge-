"""
Problem statement :
    Program TO find sum of Digits.
    Input : Any integer positive Number.
    Output : print sum of all its Digits.        
"""
def sum_of_digits(number):
    num_str = str(number)
    digit_sum = 0

    for digit in num_str:
        digit_sum += int(digit)

    return digit_sum


user_input = input("Enter a positive integer: ")

if user_input.isdigit():
    user_input = int(user_input)
    result = sum_of_digits(user_input)
    print(f"The sum of digits of {user_input} is: {result}")
else:
    print("Invalid input. Please enter a valid positive integer.")
