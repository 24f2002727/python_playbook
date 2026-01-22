"""
2. Problem
Write a recursive function is_palindrome(n) that returns True if a number is a
palindrome, else False.
Input:
is_palindrome(12321)
Output:
True
Constraints:
No loops
No string conversion
"""
def count_digits(n):
    if n == 0:
        return 0
    return 1 + count_digits(n // 10)

def reverse_number(n, digits):
    if n == 0:
        return 0
    return (n % 10) * (10 ** (digits - 1)) + reverse_number(n // 10, digits - 1)

def is_palindrome(n):
    digits = count_digits(n)
    return n == reverse_number(n, digits)

print(is_palindrome(12321))   # True
print(is_palindrome(123))     # False
print(is_palindrome(1))       # True