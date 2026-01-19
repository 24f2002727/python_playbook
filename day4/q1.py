"""
Problem 1
Create a tuple containing at least 6 elements.
Write a program to:
Print the first element
Print the last element
Print all elements except the first and last
"""
l=[]
for i in range(6):
   x=int(input("Enteer the data"))
   l.append(x)

tup=tuple(l)
print(tup[0])
print(tup[-1])
print(tup[1:-1]) 