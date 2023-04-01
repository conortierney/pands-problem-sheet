# week 7 task 
# Author: Conor Tierney
# count 'e's in text task
# # Program to get letter count in a text file.
# reference: www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/

FILENAME = "count_es.txt"


with open("count_es.txt", "r") as f:                 # opens the file name & path for reading.
    
    contents = f.read()                                  # Reads the contents of the file.

count = contents.count("e")                               # Use count to get the number of times the letter 'e' is in text.

print(f"This file contains the letter 'e' {count} times.")

# I used the text "Hello there. My name is Conor."  # This text has 4 'e's in it.