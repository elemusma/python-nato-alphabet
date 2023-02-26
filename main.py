student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

# with open('nato_phonetic_alphabet.csv') as alphabet:
#     contents = alphabet.read()
#     print(contents.code)

nato_alphabet = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter:row.code for (index, row) in nato_alphabet.iterrows()}
print(phonetic_dict)

# letter_list = nato_alphabet.letter.to_list()
# # code_list = nato_alphabet.code.to_list()

# letter_a = nato_alphabet[nato_alphabet['letter'] == 'A'].code.item()
# # print(str(letter_a))
# # print(nato_alphabet)

# nato_dict = {letter:nato_alphabet[nato_alphabet['letter'] == letter].code.item() for letter in letter_list}
# # print(nato_dict)

# name_dict = {new_key:new_value for item in list}

# print(nato_dict['T'])

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input("What is your first name? ").upper()
output_list = [phonetic_dict[letter] for letter in name]
print(output_list)
# name_list = list(name)
# phonetic_list = [phonetic_dict[letter] for letter in name_list]
# # print(name_list)
# print(phonetic_list)