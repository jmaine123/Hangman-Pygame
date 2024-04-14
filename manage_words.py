import pandas as pd
import requests
import pickle
import os, sys, ast





# reading the data from the file 
with open('dc_characters.txt', 'rb') as handle: 
    data = handle.read() 
  
  
# reconstructing the data as dictionary 
dc_characters = pickle.loads(data)



with open("/Users/user/Desktop/Code_Games/Hangman/words.py") as f:
    data = f.read()
    word_dict = ast.literal_eval(data)
    
word_dict.update(dc_characters)



# print(type(all_words))
