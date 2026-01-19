"""
2. Problem: You are given a list of dictionaries representing students.
students = [
{"name": "A" , "marks": 85},
{"name": "B" , "marks": 72},
{"name": "C" , "marks": 85},
{"name": "D" , "marks": 90}
]
Tasks:
1. Find the highest marks
2. Print names of all students who scored the highest
3. Store result in a dictionary like:
{
"top_score": 90,
"students": ["D"]
}
Rules:
No built-in max ()
Must use loops, conditions, and dictionaries

"""
def topper_finder(l1:list):
    topper_list=[]
    marks_dict={}
    max_marks=0

    for dictt in l1:
        marks_dict[dictt["marks"]]=[]
    for dictt in l1:
        marks_dict[dictt["marks"]].append(dictt["name"])
    for key,value in marks_dict.items():
        if key>max_marks:
            max_marks=key
            topper_list=value

    return topper_list    
students = [
{"name": "A" , "marks": 85},
{"name": "B" , "marks": 72},
{"name": "C" , "marks": 85},
{"name": "D" , "marks": 90}
]
l=topper_finder(students)
print(l)  