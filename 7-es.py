# week 7 task, es.py
# Author: Conor Tierney.
# This program reads the text file 'count_es.txt' and outputs the number of e's it contains.
# Program to get letter count in a text file.
# Ref: www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/
# Ref: https://realpython.com/working-with-files-in-python/
# Ref: https://www.w3schools.com/python/python_file_handling.asp

FILENAME = "count_es.txt"


with open("count_es.txt", "r") as f:                     # opens the file name & path for reading.
    
    contents = f.read()                                  # Reads the contents of the file.

count = contents.count("e")                              # Use count to get the number of times the letter 'e' is in text.

print(f"The file 'count_es.txt' contains the letter 'e' {count} times.")

# I used the text "Hello there. My name is Conor."  # This text has 4 'e's in it.
