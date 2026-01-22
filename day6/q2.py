"""
QUESTION 2:
Write a Python program to print a hollow butterfly pattern.
Input:
4
Output:
* *
** **
* * * *
* ** *
* ** *
* * * *
** **
* *
"""

def hollow_butterfly(n):
    # Upper half
    for i in range(1, n + 1):
        # Left wing
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        # Space between wings
        print(" ", end="")
        # Right wing
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Lower half
    for i in range(n, 0, -1):
        # Left wing
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        # Space between wings
        print(" ", end="")
        # Right wing
        for j in range(1, i + 1):
            if j == 1 or j == i:
                print("*", end="")
            else:
                print(" ", end="")
        print()


# Driver code
n = int(input())
hollow_butterfly(n)