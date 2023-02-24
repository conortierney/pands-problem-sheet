#Author: Conor Tierney
#Task 3: accounts.py
#code program called accounts.py that reads in a "10 character account number" - Part1
#and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
#my notes: add read in a string of 10 characters, not a 10 number string" ".
#reference - W3 schools, string slicing.

#Part1 - must be a 10 digit acc number// if and else  = see week 4 learnings.
bankaccnumber = input("Please enter a 10-digit account number:")
if len(bankaccnumber) != 10:
 print("Error: Account number should be exactly 10 digits long.")

else:
 bankaccnumber = "X" * 6 + bankaccnumber[6:]
 print("Bank account number: ", bankaccnumber)

#Part 2 - Extra: modified program to deal with with account no. of any length
bankaccnumber = input ("please enter a 10 digit account number:")
bankaccnumber = "X" * 6 + bankaccnumber[6:]
print("bankaccnumber: ", bankaccnumber)
