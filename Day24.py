"""
Problem statement: 
    write a program to segregate 0's and 1's an array.
    you are given an array of 0's and 1's in random order segregate os on left and 1's on right side of the array only once.
    
    Input:[0,1,0,1,0,0,1,1,1,0]
    Output:[0,0,0,0,0,1,1,1,1,1]
    
"""
def segregate(arr):
    left, right = 0, len(arr) - 1

    for i in range(len(arr)):
        # Move left pointer to the right until it encounters 1
        if arr[left] == 0:
            left += 1

        # Move right pointer to the left until it encounters 0
        if arr[right] == 1:
            right -= 1

        # Swap 0 at the left with 1 at the right
        if left < right and arr[left] == 1 and arr[right] == 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr


user_input = input("Enter 0s and 1s separated by spaces: ")
input_array = list(map(int, user_input.split()))

output_array = segregate(input_array)
print("Segregated array:", output_array)

"""
output:

D:\75 hard coding challenge>python ./Day24.py
Enter 0s and 1s separated by spaces: 0 1 0 1 0 0 1 1 1 0
Segregated array: [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

D:\75 hard coding challenge>
"""
