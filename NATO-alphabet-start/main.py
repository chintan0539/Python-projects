# Looping through dictionaries:


import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
word = {row.letter: row.code for (index, row) in nato.iterrows()}
print(word)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter yor name : ").upper()
result=[]
# result = [w ]
for a in user_input:
    result.append([w for (letter, w) in word.items() if a ==letter])

print(result)
