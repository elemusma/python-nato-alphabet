student_dict = {
    'student': ['Tadeo', 'Cuba', 'Nori'],
    'score': [56, 76, 98]
}

#Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#loop through a data frame

# for (key, value) in student_data_frame.items():
#     print(value)

#loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)