"""
1. Problem
Write a function count
_digits(n) that returns the number of digits in a positive
integer using recursion only.
Input:
count
_digits(54321)
Output:
5
Rules:
No loops
No string conversion
Use only recursion and basic arithmetic
"""
def count_digits(n):
    x=n
    if x==0:
        return 0
    return (1+count_digits(n//10))

print(count_digits(5))
print(count_digits(25))
print(count_digits(125))
print(count_digits(1125))
