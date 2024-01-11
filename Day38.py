"""
Problem statement: 
MS Excel columns  have a pattern like A,B,C,......,z,AA,AB,....AZ,BA,BB,....,ZZ,
AAA,AAB,.... etc. in other words , column 1 is named as "A", column 2 as"B", column
27 as "AA".
given a column number, find its corresponding Excel column name. the following are more examples.

input:26
output:Z

input:51
output:AY
"""
def excel_column_name(column_number):
    result = ""
    
    while column_number > 0:
        remainder = (column_number - 1) % 26
        result = chr(ord('A') + remainder) + result
        column_number = (column_number - 1) // 26
    
    return result

column_number = int(input("Enter the column number: "))

print("Excel column name:", excel_column_name(column_number))




"""
Output:

(base) E:\75 hard coding challenge>python ./Day38.py
Enter the column number: 26
Excel column name: Z

(base) E:\75 hard coding challenge>python ./Day38.py
Enter the column number: 80
Excel column name: CB

(base) E:\75 hard coding challenge>python ./Day38.py
Enter the column number: 705
Excel column name: AAC

"""

