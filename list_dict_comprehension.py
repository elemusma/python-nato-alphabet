numbers = [1, 2, 3]
new_list = []
# for n in list:
#     add_1 = n + 1

# new_list.append(add_1)
# print(new_list)

# new_list = [new_item for item in list]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Cuba"
cuba_list = [letter for letter in name]
print(cuba_list)

new_range = [num * 2 for num in range(1, 5)]
print(new_range)

names = ['Alex', 'Beth', 'Caroline', 'Eleanor', 'Freddie']
short_names = [name for name in names if len(name) < 5]
print(short_names)
uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)
import random

# students_scores = {new_key:new_value for item in list}
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# passed_students = {student:students_scores[student] for student in names if students_scores[student] > 60}
passed_students = {student:score for (student, score) in students_scores.items() if score > 60}

print(passed_students)