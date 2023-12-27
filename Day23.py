"""
Problem statement: 
    write a program to find out distance between two points if coordinates of two points are given.
    
    Input:x1,y1=(3,4)
          x2,y2=(7,7)
    Output:5
    
    Input:x1,y1=(3,4)
          x2,y2=(4,3)
    Output:1.41421
    
"""
import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))


x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

result = calculate_distance(x1, y1, x2, y2)


print(f"Distance between ({x1},{y1}) and ({x2},{y2}): {result}")


"""
Output:

PS D:\75 hard coding challenge> python .\Day23.py
Enter the x-coordinate of the first point: 3
Enter the y-coordinate of the first point: 4
Enter the x-coordinate of the second point: 7
Enter the y-coordinate of the second point: 7
Distance between (3.0,4.0) and (7.0,7.0): 5.0
PS D:\75 hard coding challenge> python .\Day23.py
Enter the x-coordinate of the first point: 3
Enter the y-coordinate of the first point: 4
Enter the x-coordinate of the second point: 4
Enter the y-coordinate of the second point: 3
Distance between (3.0,4.0) and (4.0,3.0): 1.4142135623730951
PS D:\75 hard coding challenge>

"""