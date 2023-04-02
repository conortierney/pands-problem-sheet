# bank.py
# Author: Conor Tierney
# week 2 task
# This program prompts the user to enter 2 money amounts (in cents)
# Then add the 2 amounts and print out the the answer with a euro sign and ecimal point.

amt1 = int(input("enter amount1(in cents):"))               # read in an integer & print it out.
print (f"the amount is {amt1}")

amt2 = int(input("enter amount2(in cents):"))               # read in a second integer and print it out.
print (f"the amount is {amt2}")

amttotal  = (amt1 + amt2)/100                               # add the 2 amounts

print (f"the sum of these is: €{amttotal}")                 # print out/ formatting of the answer in €.
