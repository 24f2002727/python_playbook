"""
Problem2
Write a program that:
Takes total marks and obtained marks
Calculates percentage
Prints:
Percentage
Pass if ≥ 40 else Fail
Example:
Total = 500
Obtained = 325
Output:
65.0
Pass
"""
total_marks=int(input("Enter the total marks: "))
obtained_marks=float(input("Enter the obtained marks : "))
percentage_obtained=obtained_marks/total_marks*100
print(f"Percentage obtained : {percentage_obtained}")
if percentage_obtained>40:print("Pass")
else :print("Fail")