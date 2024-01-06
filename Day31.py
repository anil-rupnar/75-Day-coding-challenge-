"""
Problem statement: 
write a program to merge two sarted arrays, the idea is to stored arrays and marge them such that the resultant arrat is aslo stored.

"""
def merge_sorted_arrays(arr1, arr2):
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # Add remaining elements from both arrays, if any
    result.extend(arr1[i:])
    result.extend(arr2[j:])

    return result


arr1 = list(map(int, input("Enter the first sorted array (space-separated): ").split()))
arr2 = list(map(int, input("Enter the second sorted array (space-separated): ").split()))

merged_array = merge_sorted_arrays(arr1, arr2)
print("Merged Array:", merged_array)



"""
Output:

(base) E:\75 hard coding challenge>python ./Day31.py
Enter the first sorted array (space-separated): 0 1 2 3
Enter the second sorted array (space-separated): 5 6 7 8
Merged Array: [0, 1, 2, 3, 5, 6, 7, 8]


"""