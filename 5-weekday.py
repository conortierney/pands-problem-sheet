# Week 5 task: weekday.py
# weekday.py
# Author: Conor Tierney.
# This program imports a built in date time function and 
# outputs if today is a weekday or a weekend day.
#ref: https://docs.python.org/3/library/datetime.html
# ref: Real Python : python 3 cheat sheet: chapters 3 and 4.



import datetime                                    # use import function, datetime: python built in functions.

today = datetime.datetime.today().weekday()        # define if today is a weekday as an integer.

if today < 5:                                      #if statement today = weekday (<5,  0= Monday)
    print("Oh no, today is a weekday, sorry!.")
else:                                              # else statement = today is a weekend day (6= sunday)
    print("Happy days, today is a weekend day.")

# program prints a message depending what day it is.
