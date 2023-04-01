# squareroot.py
# week 6 task
# This program prompts the user to enter a positive number as input,
# and outputs an approximation of its squareroot.
# Author: Conor Tierney

def sqrt():                                                   # define (def) a new function for square root.
    
    while True:                                               # while loop to ensure number entered is positive.
        try:
            x = float(input("Please enter a positive number: "))     # Prompt the user to enter a positive number
            if x > 0:
                break                                         # while loop stops if user enters positive number.
            else:
                print("incorrect,the number must be positive")     # else: print error message.
        except ValueError:
            print("incorrect input,enter a positive number")
                                                       
    sqroot = x / 2                                                    # initial guess of sqroot for the positive number.                                        
     
    while True:
        
        new_guess = 0.5 * (sqroot + x / sqroot)                       # estimate square root using newton method.
        
        
        if abs(new_guess - sqroot) < 1e-9:
            return new_guess
        
        
        sqroot = new_guess                                       # update the program for the new guess


print(f"The square root of this is: {sqrt()}")                  # output the result in a string format for result.