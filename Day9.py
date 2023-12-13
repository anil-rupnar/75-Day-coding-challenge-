"""
Problem statement :
    find out secand largest number of 3 numbers.
    Input : three integer separated by space denoting the numbers to be compared to find secand largest Number.
    Output : Smallest number out of the Three given number.
        
"""
def second_largest_number(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    return numbers[1]


input_numbers = input("Enter three integers separated by space: ")
num_list = list(map(int, input_numbers.split()))

if len(num_list) == 3:
    result = second_largest_number(num_list[0], num_list[1], num_list[2])
    print(f"The second-largest number is: {result}")
else:
    print("Please enter exactly three integers.")
    
