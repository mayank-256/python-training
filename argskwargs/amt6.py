employees = [
    {"id": 101, "name": "John", "salary": 50000},
    {"id": 102, "name": "Alice", "salary": 65000},
    {"id": 103, "name": "Bob", "salary": 45000},
    {"id": 104, "name": "David", "salary": 70000},
]

# Tasks
# Find the employee with the highest salary.
# Calculate the average salary.
# Display employees earning above average.
# Increase salary by 10% for employees earning less than 50,000.
# Sort employees by salary.

sly=[]
# def highest_salary():
#     """Find the highest salary"""
#     for i in range(len(employees)):
#         sly.append(employees[i]["salary"])
#     sly.sort()
#     return(sly[-1])

# print(highest_salary())

# def average():
#     """"find the average salary """
#     for i in range(len(employees)):
#         sly.append(employees[i]["salary"])
#     return {sum(sly)/len(sly)}
# a = average()
# print(a)

# def above_avg():
#     """find above average"""
#     for i in range(len(employees)):
#         sly.append(employees[i]["salary"])
#     average = sum(sly)/len(sly)
    
#     for i in range(len(employees)):
#         if (employees[i]["salary"]) > average:
#             print(employees[i])
#     return f"Data of student above average({average})"
# ans = above_avg()
# print(ans)

# def increase_salary():
#     """increase salary by 10% of salary below 50000"""
#     for i in range(len(employees)):
#         if employees[i]["salary"] < 50000:
#             employees[i]["salary"] +=  (employees[i]["salary"] * 10)/100
#     print(employees)
#     return"10 %/ increased salary for employee with less than 50000"
# increase_salary()


x = 1.0//2
print(x)