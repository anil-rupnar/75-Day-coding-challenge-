"""
Problem Statement : 7. Reverse Integer

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

"""
class Solution(object):
    def reverse(self, x):
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        sign = 1 if x >= 0 else -1
        x = abs(x)
  
        # Reverse the digits
        reversed_x = 0
        while x != 0:
            digit = x % 10
            x = x // 10

            if reversed_x > (INT_MAX - digit) // 10:
                return 0
            reversed_x = reversed_x * 10 + digit
        
        # Apply the original sign
        reversed_x *= sign
  
        if reversed_x > INT_MAX or reversed_x < INT_MIN:
            return 0
        
        return reversed_x

solution = Solution()
print(solution.reverse(123))   
print(solution.reverse(-123))  
print(solution.reverse(120))   