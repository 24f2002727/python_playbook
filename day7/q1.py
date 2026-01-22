"""
1. Problem
Write a program that:
1. 2. 3. Reads integers from a file numbers.txt (one number per line)
Ignores invalid lines (non-integers) using error handling
Prints the sum of valid integers
Example numbers.txt
10
20
abc
30
Output
Sum = 60
Rules:
Must use with
Must use try–except
No program crash allowed
"""
sum=0
try:
    with open("numbers.txt","r") as file:
        data=file.readline()
        while(data):
            try:
                data=int(data)
                sum+=data
            except:
                sum+=0
            data=file.readline()

except FileNotFoundError:
    print("File not exists")

print(sum)