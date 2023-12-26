"""
Problem statement: 
    write a program find LCM of two numbers.

    Input:15 20
    Output:60
    
    Input:15 25
    Output:75
    
"""
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

def main():
    try:
        
        num1, num2 = map(int, input("Enter two numbers separated by space: ").split())

        result = lcm(num1, num2)
        print("LCM of", num1, "and", num2, "is:", result)

    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
