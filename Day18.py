"""
Problem statement: 
    given stored array with many duplicate elements, the program is to find indexs of first and last occurances of an element x in given array start index from 0.
    
Input format:first line of the input is number of element N array element in second line
            in sample input ,there are 10 elements in an  array[1 2 2 2 2 3 4 8 8 8] and element to be searched(x) is 8.
            so ,output is 7 and 9.
example:
    input:arr[]={1,2,2,2,2,3,4,8,8,8}
            x=8
    output:first occurance =7
           last occurance =9
"""
def find_first_last_occurrences(arr, x):
    first_occurrence = -1
    last_occurrence = -1

    for i in range(len(arr)):
        if arr[i] == x:
            if first_occurrence == -1:
                first_occurrence = i
            last_occurrence = i

    return first_occurrence, last_occurrence


n = int(input("Enter the number of elements in the array: "))
arr = list(map(int, input("Enter the array elements separated by space: ").split()))
x = int(input("Enter the element to be searched: "))


first, last = find_first_last_occurrences(arr, x)

print("First occurrence:", first)
print("Last occurrence:", last)
