# squareroot.py
# Week 6 task.
# Author: Conor Tierney
# This program prompts the user to enter a positive number as input.
# and outputs an approximation of its squareroot using the newton method at estimating square roots.
# Ref: https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula
# Ref: https://www.youtube.com/watch?v=xdlIFw5EM4w



def sqrt():                                                   # define (def) a new function for square root.
    
    while True:                                               # while loop to ensure number entered is positive.
        try:
            x = float(input("Please enter a positive number: "))     # Prompt the user to enter a positive number.
            if x > 0:
                break                                         # while loop stops if user enters positive number.
            else:
                print("incorrect,the number must be positive")     # else: print error message if negative number or incorrect input.
        except ValueError:
            print("incorrect input,enter a positive number")

                                        
    approx = x / 2                                                    # assume approx as half the number.                                        
    while True:
        
        better = 0.5 * (approx + x / approx)                       # find a better value using newton method.
        
        if abs(better - approx) < 1e-9:
            return better
        
        approx = better                                            # assume founfd better value as approx.

print(f"The square root of this is approx: {sqrt()}")                  # output the result in a string format for result.
