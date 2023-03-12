#Task 4: collatz.py
#Author : Conor Tierney.

# This program asks the user to input a positive integer stored as "number".
# at each stage of the loop, the program updates the number value based on whether it is even or odd.
# if number is even, divide // n by 2.
# if number is odd, x n by 3 and add 1.
# when number becomes 1, the program ends.

#referneces: W3schools, realpython.com (whileloops), 
#ref: AUTOMATE THE BORING STUFF WITH PYTHON - flow control.


n = int(input("Please enter a positive integer: "))   #ask user to input a positive number.

while n != 1:                                         #while number is not equal to 1,
    print(n, end=" ")                                 #print the value of the number.
    if n % 2 == 0:                                    #if number is even,
        n = n // 2                                    # program divides number by 2.
    else:                                             #if number is odd,
        n = 3 * n + 1                                 # program multiplies number by 3 and add 1

print(n,end=" ")                                      #when the number =1, program prints final value.  


















