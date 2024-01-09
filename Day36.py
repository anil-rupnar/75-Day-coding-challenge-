"""
Problem statement: 
Given two positive integers N and X , where N is the number of total patients and X
is the time duration (in minutes) after which a new patient arrives. aslo , docter will
givethe last patient needs to wait.

Test cases:

Input:
the input denote the total number of patients N and the time interval x (in minutes)in which
the next patients are visiting.

Output:
the waiting time of last patient.

input: 4 5
output: 15
"""

def calculate_waiting_time(N, X):
    return (N - 1) * 10 - (N - 1) * X

def process_test_cases(test_cases):
    for N, X in test_cases:
        result = calculate_waiting_time(N, X)
        print(result)

T = int(input("Enter the number of test cases: "))


test_cases = []

for _ in range(T):
    N, X = map(int, input("Enter N and X for a test case (separated by space): ").split())
    test_cases.append((N, X))

process_test_cases(test_cases)



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

