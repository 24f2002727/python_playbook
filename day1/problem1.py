"""
Problem1
Build a program that:
Takes two numbers
Prints:
Their sum
Their difference
Their product
The bigger number
"""
n1=int(input("Enter the first no."))
n2=int(input("Enter the second no."))
print(f'Sum of the given no {n1} and {n2} is: {n1+n2}')
print(f'Difference of the given no {n1} and {n2} is: {n1-n2}')
print(f'Product of the given no {n1} and {n2} is: {n1*n2}')
print(f'Biggest of the given no {n1} and {n2} is: {max(n1,n2)}')