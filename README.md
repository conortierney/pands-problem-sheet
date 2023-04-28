# Programming and Scripting 2023

## Pands- Problem- Sheet

### Author: Conor Tierney

## Contents Table

*File Description  

*Weekly Tasks
  1. HelloWorld!
  2. bank.py
  3. accounts.py
  4. collatz.py
  5. weekday.py
  6. squareroot.py
  7. es.py
  8. plottask.py  
  
* README.md file resource
* Software:  


### Description
This readme file is related to the tasks outlined for the pands problem sheets for Programming and Scripting module in HDip in computing in Data Analytics at ATU.

The file here will explain the code, input and output for each task. It will also reference any sources used to solve and test the tasks.

Most of my problem solving for the tasks was gained throught practicing python coding in Andrew Beatty's lectures and weekly labs.

VSCode sofware is used to code the programs.  
___


### Weekly Tasks

## *Hello World!*

Task 1 of the PANDS Problem Sheet was download and istall the software needed for the module. These were cmder (windows), anaconda, vscode, git and notepad++. After the required software was insatlled on my machine I created my github account and two repositories called ''mywork'' and ''pands-problem-sheet".

The pands-problem-sheet contains a python program that displays ***Hello World!*** when it is run. This is task 1.

***code***  
`print ("helloworld!")`

***user output:***  
`helloworld!`  

___

## bank.py

This program is called bank.py. When banks are storing currency figures, they store them as integers (usually in cents).
this is to avoid rounding errors.

*This program:*
 * *Prompts the user to read in 2 money amounts in cents.*
 * *Then adds the 2 amounts entered.*
 * *Then prints out the answer in a readable format with a euro sign and a decimal point between the euro and cent of the amount.*
 
***Note:*** the idea here is to break the task down into smaller parts as I am new to coding. Read in the first amount and print it back out, then read in the second amount and add the two. Then format the answer.
The answer is formated so that the total amount has the euro sign and a decimal point.

The program uses calculation of the given code based on the users in put of 2 numbers.

**Screenshot of bank.py code from my VSCode ( saved in issues on github)**
![image](https://user-images.githubusercontent.com/123323783/230906661-19ba745c-17e3-432d-afcf-6dd9284c2b0a.png)

***user calls:***  
`python bank.py`

***user input:***  
`enter amount1(in cents):65`

`enter amount2(in cents):180`


***output:***  
`the sum of these is: €2.45`

***References/sources:***  
[W3 SCHOOLS NUMBERS](https://www.w3schools.com/python/python_numbers.asp)  
[Using f string](https://realpython.com/python-f-strings/)  

___

## accounts.py  

This program is called accounts.py.  

**The task was to:**
*Write a python program called accounts.py that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).*
*Extra: Modify the program to deal with account numbers of any length*  

Context: bank account numbers can be stored as 10 character strings, some applications only display the last 4 characters(digits) with the first 6 characters displayed as X's for security reasons.  

The 1st part of the program prompts the user to enter a 10 digit number. This is a string of 10 characters and not a 10 number string.
The *if* statement checks that exactly 10 digits are entered, if not the program outputs and ERROR message.
Then the *else* statement is used to print the account number with only the last 4 digits showing.  

Part 2: The program is modified to deal with user input of an acoount of any length.  

***user calls:***  
`python accounts.py`  

***user input 1:***  
`Please enter a 10-digit account number:0987654321` 

***output:***    
`Bank account number:  XXXXXX4321`  

***user input 2:***  
`please enter an account number(any length):112233`  

***output:***  
`bankaccnumber:  XXXXXX`  

 ***References/sources:*** 
[A Whirlwind Tour of Python]  
[geeksforgeeks.org](https://www.geeksforgeeks.org/string-slicing-in-python/)  

___

## collatz.py  

This program is called collatz.py.  
*It asks the user to input any positive integer and outputs the successive values of a calculation in the program. At each step it calculates the next value by taking the current value and, if it is even, divides it by two, but if it is odd, multiplies it by three and add's one. The program ends if the current value is equal to one*


I added some code to handle negative numbers in the program. I did this using a while loop and an error message so that the user is prompted again to enter a POSITIVE number.

In the program, I check if a number is odd or even by using another *while* loop. The program keep doing this until it reaches the number 1.  
*If* and *else* statements are used.  
If the number is even, it's divided by 2 and print the result. If the number is odd, it's multiplied by 3 and add 1, and then print the result.  

***user calls:***  
`python collatz.py`

***user input:***  
`Please enter a positive number: 13`  

***output if positive number entered:***  
`13 40 20 10 5 16 8 4 2 1`  

***user input:***  
`Please enter a positive number: -12`  

***output if negative number entered:***  
`-12 :isn't a positive number.`
`Enter a positive number:`  

***References/sources:***  
[W3schools, realpython.com (whileloops]  

[AUTOMATE THE BORING STUFF WITH PYTHON- flow control]  



___

## weekday.py  

This program is called weekday.py  

*This program outputs whether or not today is a weekday*

The import function for date time is used (python built in functions).
***code***
`import datetime`  

Today is then defined if today is a weekday as an integer.  

***code***
`today = datetime.datetime.today().weekday()`  # where monday =0 and Sunday= 6.  

The *if* statement is used to check if today is a weekday. If it is not a weekday when the program is run the *else* statement is used to let the user know it is a weekend day. 
The program will have different ouptputs depending on the day the prorgam is run.

It's important to run the program on both the weekday and weekend to get a correct result.  

***user input:***  
`python weekday.py`  

*this program does not requre any user input, it just outputs the result*  


***If its run on a weekday, the program output is:***  
`Oh no, today is a weekday, sorry!.`  

***If its run at the weekend, the program output is:***  
`Happy days, today is a weekend day.`  

 ***References/sources:***  
 [docs.python.org](https://docs.python.org/3/library/datetime.html)[library/datetime]  
 [Real Python : Python 3 cheat sheet: chapters 3 and 4]  
 

___

## squareroot.py

This program is called squareroot.py  

* *The program that takes a positive floating-point number as input and outputs an approximation of its square root.*  
* *The task asks to create your own sqrt function and not to use the built in functions x ** .5 or math.sqrt(x).*
* *This is to demonstrate that you can research and code a process.*
* *It is suggested suggested to look at the newton method at estimating square roots*  


The code defines a function called sqrt `def sqrt():` that calculates the square root of a positive number entered by the user. The function uses a *while* loop to prompt the user to enter a positive number and to ensure that the entered number is positive. 
When a positive number is entered, the function initializes a guess for the square root and starts another *while* loop to calculate a better approximation for the square root using the Newton-Raphson method. 
The loop continues until the difference between the new approximation and the previous approximation is less than *1e-9*, at which point the function returns the final approximation for the square root. 
Finally, the function is called and the resulting approximation is printed to the console.

The program code is a simple implementation of the Newton-Raphson method for approximating the square root of a number.  

***user input:***  
`python squareroot.py`  

***output:***  
`Please enter a positive number: 10`  
`The square root of this is approx: 3.162277660168379`  

***when a positive number is not entered***  
`incorrect,the number must be positive`  
`Please enter a positive number:`  


***References/sources:***  
[tutorialsinhand.com](https://tutorialsinhand.com/Articles/python-program-to-find-square-root-of-a-number-using-newton-square-root-formula)  
[youtube: the last minute professor](https://www.youtube.com/watch?v=xdlIFw5EM4w)  

___

## es.py  

This program is called es.py. It runs with a text file called `count_es.txt`  

*The requirement is to write a program that reads in a text file and outputs the number of e's it contains.*  
*The program should take the filename from an argument on the command line*

The text file `count_es.txt` contains the text 'Hello there. My name is Conor.'  
It contains the letter 'e' 4 times.

The program reads in the file name `FILENAME = "count_es.txt"`  
To read the file that we specified , we use the `open(filename, 'r')` function. This makes the file available for reading only. 
To count the number of lowercase letter "e" in the file, we use the `count()` method with the argument "e" as a string.  


***user input:***  
`python es.py`  

***output:***  
`The file 'count_es.txt' contains the letter 'e' 4 times.`  

***References/sources:***  

[https://realpython.com/working-with-files-in-python/]  
[https://www.w3schools.com/python/python_file_handling.asp]


___

## plottask.py  

This program is called plottask.py.  

The task was to write a program that displays:
* a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
* and a plot of the function  h(x)=x3 in the range [0,10],
* on the one set of axes.
* marks are be given for making the plot look nice (legend etc).  

The code generates two distributions and displays them on a single graph. The first distribution is a normal distribution with 1000 values and a mean of 5 and a standard deviation of 2. This distribution is displayed as a histogram.

The second distribution is an exponential distribution function defined as h(x) = x3, with x values ranging from 0 to 10. This distribution is also displayed on the same set of axes as the normal distribution histogram.

To create and display the histogram, the code uses the Python libraries `NumPy` and `Matplotlib`. NumPy is used to generate the values for the normal distribution and Matplotlib is used to plot the histogram and the exponential distribution function on the same set of axes.

The histogram is generated using the `plt.hist()` function and shown with the `plt.show()` function. The line graph is generated using the `plt.plot()` function and shown with the `plt.show()` function. The plots are displayed side by side using the `plt.subplot()` and `plt.subplots_adjust()` functions. The x and y axis labels and the titles of the plots are also defined using the `plt.xlabel(), plt.ylabel(), and plt.title()` functions.


***user input***  
`python plottask.py`

**NOTE: This program is not currently working for me as I am getting an error message in the terminal**
**OMP: Error #13: Assertion failure at kmp_affinity.cpp(532).***


___

## README.md file resource  

[mark down guide](https://www.markdownguide.org/basic-syntax#headings)  

(https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)  

___

## Software:  

* Visual Studio Code - version: 1.76.2  
