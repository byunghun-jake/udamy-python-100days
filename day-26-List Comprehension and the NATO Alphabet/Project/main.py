import pandas
# TODO 1. Create a dictionary in this format:
#   {"A": "Alfa", "B": "Bravo"}
data_frame = pandas.read_csv("./nato_phonetic_alphabet.csv")

# data_frame을 순환
data_dict = {row.letter:row.code for (index, row) in data_frame.iterrows()}
print(data_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
input_text = input("Enter a word: ").upper()

result = [data_dict[letter] for letter in input_text]
print(result)