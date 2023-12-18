"""
Problem statement :
    write a pyhton program to print Box number pattern of 1 and 0.
    Input :Given a single line separated by spcae. N1 denotes the Numbers of rows N2
    denotes the numbers of columns.
    Output : print the output in the format.
    
"""
def box_pattern(rows, columns):
    for i in range(rows):
        for j in range(columns):
            
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                print("1", end=" ")
            else:
                # Print 0 for the interior of the box
                print("0", end=" ")
        print()  # Move to the next line after completing a row


input_line = input("Enter the number of rows and columns separated by space: ")
N1, N2 = map(int, input_line.split())

box_pattern(N1, N2)
