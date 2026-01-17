"""
Q3:
Given a list of integers:
- find the largest number in the list,
- find the second largest number in the list,
do not use built-in functions for finding maximum values.
"""
def max(l1:list):
    maxm=l1[0]
    for i in l1:
        if i>maxm:
            maxm=i
    return maxm

l1=[4,5,6,7,6,9]
print(max(l1))