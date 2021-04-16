import pandas
nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
    
# Keyword Method with iterrows()
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}
#print(nato_dict)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Input a word to be converted: ").upper()
output_list = [nato_dict[letter] for letter in user_input if letter != " "]
print(output_list)

# user_input = [letter for letter in user_input]

# nato_output = {letter:code for (letter, code) in nato_dict.items() if letter in user_input}
# print(nato_output)