"""
Problem statement: 
Given an array of integers , the task is to find whether it's possiblr to construct an integer using all the digits of these numbers such that it would be divisible by 3.if it is possible then print "1" and If not print "0".

test case:

Input :
arr[]={40,50,90}

Output:
1

input :
arr[]={1,4}

Output:0

"""
def is_divisible_by_3(arr):
    # Step 1: Find the sum of all digits
    total_sum = sum([sum(map(int, str(num))) for num in arr])

    # Step 2: Check if the sum is divisible by 3
    if total_sum % 3 == 0:
        return 1
    else:
        return 0

input_array = list(map(int, input("Enter space-separated integers: ").split()))

result = is_divisible_by_3(input_array)

print(result)
