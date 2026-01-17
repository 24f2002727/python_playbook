"""
Q1:
Write a program that takes an integer n and:
- checks whether the number is positive, negative, or zero,
- if the number is positive, check whether it is even or odd.
"""
def no_checker(n):
    if n==0:
        return("Inputed number is zero")
    
    if n<0:
        return("Number is negative")
    
    if n>0:
        return("Number is even" if n%2==0 else "Number is odd")
    
n=int(input("Enter the no: "))
print(no_checker(n))