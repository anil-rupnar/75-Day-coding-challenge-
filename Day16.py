"""
Problem statement :
    Program print Below pattern.
    Input :input to get on integer N.
    Output :
            1
            2*2
            3*3*3
            4*4*4*4
            4*4*4*4
            3*3*3
            2*2
            1
        
            
    
"""
def print_pattern(N):
    # Print the upper half of the pattern
    for i in range(1, N + 1):
        for j in range(1, i + 1):
            print(i, end="")
            if j < i:
                print("*", end="")
        print()

    # Print the lower half of the pattern
    for i in range(N , 0,-1):
        for j in range(1, i + 1):
            print(i, end="")
            if j < i:
                print("*", end="")
        print()


N = int(input("Enter an integer N: "))

print_pattern(N)
