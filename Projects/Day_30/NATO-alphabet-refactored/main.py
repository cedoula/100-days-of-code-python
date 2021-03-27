# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas as pd
# student_data_frame = pd.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#Create a code dictionary
code_df = pd.read_csv("nato_phonetic_alphabet.csv")
code_dict = {row.letter:row.code for (index, row) in code_df.iterrows()}


#Create a list of the phonetic code words from a word that the user inputs.
stop = False
while not stop:
    word = input("Enter a word: ").upper()
    try:
        word_encoded = [code_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        stop = True
        print([code_dict[letter] for letter in word])
