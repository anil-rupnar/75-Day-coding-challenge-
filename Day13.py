"""
Problem statement :
    Print Digits of given number in same order.
    Input : Any integer positive Number.
    Output : print Digit of the input number in same order in space separated fashan.       
"""
def print_digits_in_order(number):
   
    number_str = str(number)
    
    
    for digit in number_str:
        print(digit, end=" ")


input_number = int(input("Enter a positive integer: "))


print("Digits in the same order:")
print_digits_in_order(input_number)
