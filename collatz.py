#collatz.py
# Week 4 task
#Author : Conor Tierney.

# This program asks the user to input a positive integer stored as "number".
# at each stage of the loop, the program updates the number value based on whether it is even or odd.
# if number is even, divide // n by 2.
# if number is odd, x n by 3 and add 1.
# when number becomes 1, the program ends.

#ref: W3schools, realpython.com (whileloops), 
#ref: AUTOMATE THE BORING STUFF WITH PYTHON - flow control.


number = int(input("Please enter a positive integer: "))     # ask user to input a positive number.

while number != 1:                                           # while number is not equal to 1,
    print(number, end=" ")                                   # print the value of the number.
    if number % 2 == 0:                                      # if number is even,
        number = number // 2                                      # program divides number by 2.
    else:                                               # else: if number is odd,
        number = 3 * number + 1                                   # program multiplies number by 3 and add 1

print(number,end=" ")                                        # when the number =1, program prints final value.  
