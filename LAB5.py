1
print(f"Task 1.1")
ans1_1 = list(input().lower())
print(ans1_1)
1.2
print(f"\nTask 1.2")
ans1_2 = {}
for x in ans1_1:
    if x in ans1_2:
        ans1_2[x] += 1
    else:
        ans1_2[x] = 1
arr = [x for x in ans1_2.items()]
print(arr)
1.3
print(f"\nTask 1.3")
vowels = "auioe"
list_vow = [i for i in ans1_2 if i in vowels]
list_cons = [i for i in ans1_2 if i.isalpha() and i not in vowels]
list_symb = [i for i in ans1_2 if not i.isalpha()]
print(list_vow, '\n', list_cons, '\n', list_symb, sep="")
1.4
print(f"\nTask 1.4")
# arr = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4]
arr = [1, 5, 8, 7, 9, 6, 7, 5, 8, 3, 9, 10, 2, 1, 3, 4, 8, 9]
addZeroCnt = 4 - len(arr) % 4
arr += [0 for i in range(addZeroCnt)]
arr.sort()
arr_size = len(arr)
q1 = arr[:arr_size // 4]
q2 = arr[arr_size // 4:2 * arr_size // 4]
q3 = arr[2 * arr_size // 4:3 * arr_size // 4]
q4 = arr[3 * arr_size // 4:]
print(q1, q2, q3, q4, sep='\n')
2
print(f"\nTask 2.1")
name = "Adam"
assignment = [82, 56, 44, 30]
lab = [78.20, 77.20]
test = [78, 77]

student = {
    "name": name,
    "assignment": assignment,
    "test": test,
    "lab": lab
}
print("student = ", student)
2.2
print(f"\nTask 2.2")
submission_check = {
    student["name"]: len(student["assignment"]) + len(student["test"]) + len(student["lab"])
}
print(submission_check)

print(f"\nTask 2.3")
if submission_check[student["name"]] >= 4:
    student["final_grade"] = 0.3 * sum(student["assignment"]) + 0.2 * sum(student["test"]) + 0.5 * sum(student["lab"])
else:
    student["final_grade"] = 0

print("student =", student)
2.4
print(f"\nTask 2.4")
student = {'name': 'Adam', 'assignment': [82, 56, 44, 30], 'test': [78, 77], 'lab': [78.2, 77.2], 'final_grade': 70.25}
student2 = {'name': 'Kevin', 'assignment': [82, 30], 'test': [], 'lab': [78.2], 'final_grade': 0}
students = {
    "Adam": student,
    "Kevin": student2
}
print(students)
3
print(f"\nTask 3.1")
transactions = [(1001, 2), (1001, 1), (1003, 2), (1005, 2), (1001, 3), (1007, 1), (1007, 2), (1100, 2), (1003, 2), (1001, 1)]
stats = {}
for userID, transaction in transactions:
    if userID not in stats:
        stats[userID] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}
    stats[userID][transaction] += 1
    stats[userID]['mft'] = transaction
    if stats[userID]['lft'] is None:
        stats[userID]['lft'] = transaction

print("stats =", stats)
