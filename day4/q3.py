"""
Problem 3
Create a dictionary to store student names as keys and their marks as values.
Write a program to:
Add a new student
Update marks of an existing student
Print all students who scored more than a given value
"""
d={
    "ram":56,
    "shyam":65,
    "neta":69
}
def add_std(name:str,marks:int,dictt:dict):
    dictt[name]=marks

def update_std(name:str,marks:int,dictt:dict):
    dictt[name]=marks

name1=input("Name of student")
marks1=int(input())
add_std(name1,marks1,d)
print(d)

name2=input("Name of student")
marks2=int(input())
update_std(name2,marks2,d)
print(d)
