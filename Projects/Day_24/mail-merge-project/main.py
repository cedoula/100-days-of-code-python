#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
from pathlib import Path

path_names = Path(__file__).parent / "./Input/Names/invited_names.txt"
path_template = Path(__file__).parent / "./Input/Letters/starting_letter.txt"

with open(path_template, "r") as file:
    template = file.read()

with open(path_names, "r") as file:
    list_names = file.readlines()

for i in range(len(list_names)-1):
    list_names[i] = list_names[i].strip()

output_path = Path(__file__).parent / "./Output/ReadyToSend/"
for name in list_names:
    letter = template.replace("[name]", name)
    with open(f"{output_path}/letter_for_{name}.txt", "w") as file:
        file.write(letter)
