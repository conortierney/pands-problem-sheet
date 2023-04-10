#Author: Conor Tierney
#Task 3: accounts.py
#code program called accounts.py that reads in a "10 character account number" - Part1
#and outputs the account number with only the last 4 digits showing (with the first 6 digits replaced with Xs).

#my notes: add read in a string of 10 characters, not a 10 number string" ".
#reference - W3 schools, string slicing.


#Part 1 - must be a 10 digit acc number// if and else.

bankaccnumber = input("Please enter a 10-digit account number:")            #user asked to enter a 10 digit number.
if len(bankaccnumber) != 10:                                                #print error if number not equal to 10 digits.
 print("Error: Account number should be exactly 10 digits long.")

else:
 bankaccnumber = "X" * 6 + bankaccnumber[6:]                             #output the acc number with only last 4 digits showing
 print("Bank account number: ", bankaccnumber)

#Part 2 - Extra: modified program to deal with with account no. of any length

bankaccnumber = input ("please enter an account number:")
bankaccnumber = "X" * 6 + bankaccnumber[6:]                       # no print error if not 10 digits
print("bankaccnumber: ", bankaccnumber)

