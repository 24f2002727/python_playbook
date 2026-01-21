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
def reverser(n):
    if n//10==0:
        return 1
    return(n%10*10+is_pallindrome(n//10))


def is_pallindrome(n):
    reverse=reverser(n)
    print(reverse)
    if n==reverse:
        return True
    return False
print(is_pallindrome(1))
print(is_pallindrome(12))
print(is_pallindrome(121))
print(is_pallindrome(1234321))