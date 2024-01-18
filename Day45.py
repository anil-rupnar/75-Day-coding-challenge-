"""
There are n students in a class, each in possession of a different funny story. As the students were getting bored in the class, they decided to come up with a game so that they can pass their time. They want to share the funny stories with each other by sending electronic messages. Assume that a sender includes all the funny stories he or she knows at the time the message is sent and that a message may only have one addressee. What is the minimum number of messages they need to send to guarantee that everyone of them gets all the funny stories?

Examples: 

Input : an integer n denoting the number of students.
Output : print the minimum number of messages they need to send to guarantee. that everyone of them gets all the funny stories.

Input : 15
Output : 28

"""
n = int(input("Enter the number of students: "))
result = 2 * n - 2
print(result)

"""
output :
(base) E:\75 hard coding challenge>python ./Day45.py
Enter the number of students: 5
8

(base) E:\75 hard coding challenge>python ./Day45.py
Enter the number of students: 15
28

"""