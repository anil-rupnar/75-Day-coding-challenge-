"""
Problem statement: 

Lohia, gosu, and Prince are footballers. Lohia and Gosu are strikers while Price is a goalkeeper. You as the coach held a practice session shootouts to improve the performance of the stickers your task is to find the maximum goal scorer between the two Lohia, gosu, and prince energy denoted by x,y, and z respectively. for every goal scored the energy of the respective player is decreased by 1 and after every save price energy is decreased by 1. Stickers will be able to store the goal of the prince. energy is a factor of their energy otherwise not.
the session ends when the prince's energy reaches 1. Assuming the same player can try for goals repeatedly and they both try to increase the number of goals in totality. lohia being a junior player is always favored for penalty kicks.

Input :
the first line of input contains an integer T denoting the number of test cases. each test case contains energy 3 integers x, y & z denoting the energies respectively.

Output :
for each test case print the number of goals scored by Lohia and Gosu respectively.
"""
def find_max_goal_scorer(x, y, z):
    goals_lohia = 0
    goals_gosu = 0

    while z > 1:
        if x >= y:
            goals_lohia += 1
            x -= 1
        else:
            goals_gosu += 1
            y -= 1

        z -= 1

    return goals_lohia, goals_gosu

def main():
    T = int(input("Enter the number of test cases: "))

    for _ in range(T):
        x, y, z = map(int, input().split())
        goals_lohia, goals_gosu = find_max_goal_scorer(x, y, z)
        print(goals_lohia, goals_gosu)

if __name__ == "__main__":
    main()


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

