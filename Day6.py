"""
Problem statement :
    write a program to find  sum of all pssible prime numbers within the range.
    Input : two +ve integers separated by space denting start and end f range.
    Output : sum of all pssible prime numbers within the range separated by range.
    
"""
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(start, end):
    prime_sum = 0

    for num in range(start, end + 1):
        if is_prime(num):
            prime_sum += num

    return prime_sum


try:
    start, end = map(int, input("Enter two positive integers separated by space (start end): ").split())
    if start < 0 or end < 0:
        raise ValueError("Both integers must be positive.")
except ValueError as e:
    print(f"Error: {e}")
else:
    
    result_sum = sum_of_primes(start, end)
    print(f"Sum of prime numbers between {start} and {end}: {result_sum}")
