"""
Given a series 2, 10, 30, 68, 130 … Identify the pattern in the series and find the nth value in the series. Indices are starting from 1 . 1 <= n <= 200

Examples: 

Input : n = 12
Output : 1740

Input : n = 200
Output : 8000200

"""
n = int(input("Enter the index (X): "))

# Calculate the term at the given index using the identified pattern
result = n**3 + n

print(result)


"""
(base) E:\75 hard coding challenge>python ./Day44.py
Enter the index (X): 8
520

(base) E:\75 hard coding challenge>python ./Day44.py
Enter the index (X): 12
1740

(base) E:\75 hard coding challenge>
"""
