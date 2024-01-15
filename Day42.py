"""
Problem statement: 
You are a traveller, lost in a jungle. but you have the map with you. and you remember the rote you travelled so you will backtrack and reach the starting point. your task is to print the starting point.

Input :
find line consists of t test cases each test case consists of 3 lines. the first line of each test case consists of two integers x, and y denoting your current location. the second line of each test case consists of an integer n denoting of number of paths you travelled. the third line of each test case consists of 2 * N spaced integers xi, yj denoting the points at the paths you travelled.

Output :
print the starting point in the respective line.


test case:
input :
1 1
2
1 0 0 1

output:
0 0


"""
def find_starting_point(x, y, n, paths):
    start_x = x
    start_y = y

    for i in range(n):
        start_x -= paths[2 * i]
        start_y -= paths[2 * i + 1]

    print("Starting point in respective line:", start_x, start_y)


t = int(input("Enter the number of test cases: "))

for _ in range(t):
    print("Enter the test case:")
    x, y = map(int, input("Enter two integers x, y: ").split())
    n = int(input("Enter the number of paths: "))
    paths = list(map(int, input("Enter the path points: ").split()))

    find_starting_point(x, y, n, paths)

"""
Output:

(base) E:\75 hard coding challenge>python ./Day42.py
Enter the number of test cases: 2
Enter the test case:     
Enter two integers x, y: 1 1
Enter the number of paths: 2
Enter the path points: 1 0 0 1
Starting point in respective line: 0 0
Enter the test case:
Enter two integers x, y: 3 4
Enter the number of paths: 3 
Enter the path points: 1 2 2 2 1 1
Starting point in respective line: -1 -1

(base) E:\75 hard coding challenge>
"""
