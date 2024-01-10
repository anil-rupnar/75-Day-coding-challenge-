"""
Problem statement: 
write a program to reverse a string without using in built string reverse library
function.

"""

def reverse_string(input_str):
    reversed_str = ""
    for char in input_str:
        reversed_str = char + reversed_str
    return reversed_str

input_string = input("Enter a string: ")

result = reverse_string(input_string)

print("Original String:", input_string)
print("Reversed String:", result)




"""
Output:
(base) E:\75 hard coding challenge>python ./Day35.py
Enter a number : 100
The number which has exactly 9 divisors are 
36 100 Total :  2

(base) E:\75 hard coding challenge>python ./Day35.py
Enter a number : 200
The number which has exactly 9 divisors are
36 100 196 Total :  3

(base) E:\75 hard coding challenge>


"""

