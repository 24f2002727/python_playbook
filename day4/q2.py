"""
Problem 2
Given two lists with duplicate values:
Convert both lists into sets
Find the common elements between them
Find elements that are only present in the first set

"""
l1=[1,2,3,1,5,2,3,4,5,6]
l2=[2,4,6,8,0,2,3,4,5,6]
set1=set(l1)
set2=set(l2)
common=set.intersection(set2)
print(common)
print(set1-set2)