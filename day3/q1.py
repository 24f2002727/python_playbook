"""
1. Problem: Given a list of integers, create a new list containing only unique elements,
preserving original order.
Input:
[1, 2, 2, 3, 1, 4]
Output:
[1, 2, 3, 4]
Constraints:
Do not use set() directly for final output.
"""
def duplicate_finder(l1:list):
    l2=[]
    for i in l1:
        if i not in l2:
            # print(i)
            l2.append(i)
    return l2

input_list=[1, 2, 2, 3, 1, 4]
output_list=duplicate_finder(input_list)
print(output_list)