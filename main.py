import pandas as pd
data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for(index,row) in data.iterrows()}
#print(data_dict)

word = input("Enter a word : ").upper()
output_list = [data_dict[i] for i in word]
print(output_list)