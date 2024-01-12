"""
Problem statement: 
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 

"""
def title_to_number(columnTitle):
    result = 0

    for char in columnTitle:
        value = ord(char) - ord('A') + 1
        result = result * 26 + value

    return result


columnTitle = input("Enter the column title: ")
columnNumber = title_to_number(columnTitle)


print(f"The corresponding column number for {columnTitle} is {columnNumber}.")



"""
Output:

(base) E:\75 hard coding challenge>python ./Day39.py
Enter the column title: AA
The corresponding column number for AA is 27.

(base) E:\75 hard coding challenge>python ./Day39.py
Enter the column title: A
The corresponding column number for A is 1.

(base) E:\75 hard coding challenge> 

"""

