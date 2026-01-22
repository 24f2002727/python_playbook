"""
QUESTION 3:
Write a Python program to print a Hollow Number Hourglass Pyramid pattern.
Numbers decrease from the edges toward the center, spaces inside, and mirrored vertically.
Input:
5
Output:
123454321
12 21
1 1
1 1
12 21
123454321
"""



def hourglass(n):
    # Upper half
    for i in range(n, 0, -1):
        if i == n:
            # First line (full numbers)
            for j in range(1, n + 1):
                print(j, end="")
            for j in range(n - 1, 0, -1):
                print(j, end="")
        else:
            # Hollow lines
            for j in range(1, i + 1):
                if j == 1:
                    print(j, end="")
                else:
                    print(" ", end="")
            for j in range(i, 0, -1):
                if j == 1:
                    print(j, end="")
                else:
                    print(" ", end="")
        print()

    # Lower half
    for i in range(2, n + 1):
        if i == n:
            for j in range(1, n + 1):
                print(j, end="")
            for j in range(n - 1, 0, -1):
                print(j, end="")
        else:
            for j in range(1, i + 1):
                if j == 1:
                    print(j, end="")
                else:
                    print(" ", end="")
            for j in range(i, 0, -1):
                if j == 1:
                    print(j, end="")
                else:
                    print(" ", end="")
        print()

n = int(input())
hourglass(n)