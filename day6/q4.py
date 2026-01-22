"""
QUESTION 4:
Write a Python program to print a butterfly pattern using numbers instead of stars.
Input:
4
Output:
1 1
12 21
123 321
12344321
12344321
123 321
12 21
1 1
"""



def butterfly(n):
    # Upper half
    for i in range(1, n + 1):
        # Left side
        for j in range(1, i + 1):
            print(j, end="")
        # Space in the middle (except last line)
        if i != n:
            print(" " * (2 * (n - i)), end="")
        # Right side
        for j in range(i, 0, -1):
            print(j, end="")
        print()

    # Lower half
    for i in range(n, 0, -1):
        # Left side
        for j in range(1, i + 1):
            print(j, end="")
        # Space in the middle (except first line)
        if i != n:
            print(" " * (2 * (n - i)), end="")
        # Right side
        for j in range(i, 0, -1):
            print(j, end="")
        print()

n = int(input())
butterfly(n)