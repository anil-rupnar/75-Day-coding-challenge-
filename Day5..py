"""
Problem statement :
    write a program t find all pssible prime numbers within the range.
    Input : two +ve integers separated by space denting start and end f range.
    Output : list f all pssible prime numbers within the range separated by range.
    """
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_primes_in_range(start, end):
    primes = [num for num in range(start, end + 1) if is_prime(num)]
    return primes

input_range = input("Enter the range (start end): ").split()
start_range = int(input_range[0])
end_range = int(input_range[1])

result = find_primes_in_range(start_range, end_range)
print("Prime numbers in the range {}: {}".format((start_range, end_range), result))
