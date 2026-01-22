"""
QUESTION 1:
Write a Python program to print a hollow diamond of stars with odd rows and even rows containing
spaces.
Input:
5
Output:
*
* *
* *
* *
* *
* *
* *
* *
*
"""

def hollow_diamond(n):
    rows = 2 * n - 1
    for i in range(1, rows + 1):
        if i % 2 != 0:
            print("*")
        else:
            print("* *")


# Driver code
n = int(input())
hollow_diamond(n)