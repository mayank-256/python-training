students = [
{"name": "John", "marks": 85},
{"name": "Alice", "marks": 92},
{"name": "Bob", "marks": 78},
{"name": "David", "marks": 95},
]
topper = 0
average = 0
for i in range(len(students)):
    average += students[i]["marks"]
    if students[i]["marks"] >topper:
        topper = students[i]["marks"]
print(average/len(students))
print(topper)
average = average/len(students)



for i in range(len(students)):
    if students[i]["marks"] > ag:
        print(students[i])

marks=[]
idx=[]
for i in range(len(students)):
    marks.append(students[i]["marks"])
    idx.append(i)

def bubbleSort(marks,idx):
    n = len(marks)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if marks[j] < marks[j + 1]:
                marks[j], marks[j + 1] = marks[j + 1], marks[j]
                idx[j], idx[j + 1] = idx[j + 1], idx[j]
                
                swapped = True
        if not swapped:
            break  
    return (marks)
    # print(idx)

print(bubbleSort(marks,idx))