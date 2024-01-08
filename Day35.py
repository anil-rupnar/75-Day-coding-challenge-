"""
Problem statement: 
Given a number N, we need to find the total number of integers with exactly 9 divisors within the given range N.

Test cases:

Input:
100

Output:
236 100

Divisors of 36 = 1, 2, 3, 4, 6, 9, 12, 18, 36
Divisors of 100 = 1, 2, 4, 5, 10, 20, 25, 50, 100
"""

def count_of_no_of_divisors(num):
    count = 0
    for i in range(1, num+1):
         if(num % i == 0):
              count = count + 1
    return count

def check_9_factors(n):
    c = 0
    for i in range(1, n+1):
        if(count_of_no_of_divisors(i) == 9):
            print(i, end= " ")
            c = c + 1
    print("Total : ", end = " ")
    print(c)

n = int(input("Enter a number : " ))
print("The number which has exactly 9 divisors are ")
check_9_factors(n)


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