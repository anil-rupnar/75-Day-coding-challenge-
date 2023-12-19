"""
Problem statement :
    Program to chack existence of pair with given sum in array.
    Input :first line of input is sum,secand of input is no of elements N,third line of input is  N elements separated by a single space.
    Output : print "array has two elements with given sum " if required pair exists and print "array doesn't have two elements with given sum " if rquired pair do not exist.
    
"""
def has_pair_with_sum(arr, target_sum):
    seen_numbers = set()

    for num in arr:
        complement = target_sum - num
        if complement in seen_numbers:
            return True
        seen_numbers.add(num)

    return False

if __name__ == "__main__":
    target_sum = int(input("Enter the sum to check for: "))
    n = int(input("Enter the number of elements in the array: "))
    
    arr = list(map(int, input("Enter the array elements separated by a single space: ").split()))

    if has_pair_with_sum(arr, target_sum):
        print("Array has two elements with the given sum.")
    else:
        print("Array doesn't have two elements with the given sum.")
