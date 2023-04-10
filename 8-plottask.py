# This program is called plottask.py 
# Author : Conor Tierney.
# Ref: https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
# Ref: https://matplotlib.org/stable/plot_types/index.html

# The program displays:
# 1) A histogram with a normal distribution of a 1000 values,
# with a  mean(loc) of 5 and standard deviation (scale) of 2.

# 2)Also, an exponential distribution function  h(x)=x3 in the range [0, 10],on the one set of axes.

# It uses the Numpy and Matplotlib libraries to genereate and display a histogram.

# step 1: Histogram

import numpy as np                               # import numpy as np as in labs.
import matplotlib.pyplot as plt                  # import matplot as ply as in labs.

data = np.random.normal(loc=5, scale = 2, size= 1000)  # This generates 1000 random numbers, 5 = mean, 2= stdev, 1000=values

plt.hist(data, bins=50, density=True)            # Plot a histogram of the data


plt.xlabel('Values')                             # Set the x-axis label
plt.ylabel('Frequency')                          # Set the y-axis label
plt.title('plottask.py')                         # Set the plot title
plt.show()                                       # Show the plot          

# the distribution is normal, the histogram will have a bell-shaped curve

# step 2: plot if function h(x)=x3 in the range (0,10)
x = np.linspace(0, 10, 100)               # linespace rane 0,10
y = x ** 3
plt.subplot(1, 2, 2)
plt.plot(x, y)                            # plot x and y 
plt.xlabel('x')                           # x label name
plt.ylabel('h(x)')                        # y label name
plt.title('Plot of h(x)=x^3')             # name plot title as string

# Adjust the spacing between subplots
plt.subplots_adjust(wspace=0.5)

# Show the plots
plt.show()

## *terminal output in VSCODE not displaying Histogram. Error 13 displayed  - cannot fix this for now.#
