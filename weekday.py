# Week 5 task: weekday.py
# Author: Conor Tierney.
#ref: https://docs.python.org/3/library/datetime.html



import datetime                       # use import function,python built in functions.

today = datetime.datetime.today().weekday()        # define today/ weekday

if today < 5:                                    # 0 = Monday, 1 = Tuesday, || # 2 - IF statement.
    print("Oh no, today is a weekday, sorry.")
else:                                                           # else statement.
    print("Happy days, today is a weekend day.")