"""
Problem statement: 
lohia , gosu & prince are footballers. lohia and gosu are strikers while price is a goalkeeper.you as the coach held a prictice session shootouts to improve the performance of the stikers your task is to find the maximum goal scorer between the two lohia , gosu and prince energy is denoted by x,y and z respectively . for every goal scored the energy of the respective player is decreased by 1 and after every save price energy is decreased by 1. strickers will be able to sotre the goal if prince . energy is a factor of their energy otherwise not.
the session ends when princes energy reaches 1.asume same player can try for goals repectedly and they both try to increase number of goals in totality. lohia being a junior player is always favoured for penality kick.

input :
the first line of input cantains an integer T denoting the number of test cases. each test case contains energy 3 integers x , y  & z denoting the energies respectively.

output :
for each test case print the number of goals scored by lohia and gosu respectively.

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

(base) E:\75 hard coding challenge>python ./Day40.py
Enter the number of test cases: 1
3 4 5
2 2

(base) E:\75 hard coding challenge>python ./Day40.py
Enter the number of test cases: 1
4 4 4
2 1

(base) E:\75 hard coding challenge>

"""

