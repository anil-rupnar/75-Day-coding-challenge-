"""
Problem statement :
    program To find Whether a number is perfect square or not.
    Input : Any integer positive Number.
    Output : print number is not input number is perfect square failure if the input number is not a perfect square.
        
"""
def is_perfect_square(number):
    square_root = int(number**0.5)
    return f"{number} is a perfect square." if square_root**2 == number else f"{number} is not a perfect square."

user_number = int(input("Enter a positive integer: "))


result = is_perfect_square(user_number)

print(result)
