---
title: "Prac05: Grids and Files"
---

:::::::::::::::::::::::::::::::::::::: questions 

- Use the old prac sheet for now

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

1. Understand and use text files to store and load data
2. Develop simple grid-based simulations using 2-dimensional arrays: fire modelling, Game of Life
3. Apply list comprehensions to simplify code
4. Experiment with parameters to investigate how they alter the outcomes of simulations

::::::::::::::::::::::::::::::::::::::::::::::::

### Introduction

In this practical you will read and write data using text files. You will also work with some grid-based 
algorithms – testing out different values to see how their parameters affect outcomes. We will also 
look at using list comprehensions to simplify our code.

### Activity 1 - Reading a CSV File

Type in the following code, weather.py, for displaying the weather stored in a file:

```python
#
# weather.py: Print min and max temps from a file
# (source: http://www.bom.gov.au/climate/)

import matplotlib.pyplot as plt

fileobj = open(‘marchweather.csv’, ‘r’) 

# add file reading code here 
line1 = ??
line2 = ??

fileobj.close()

mins = # add splitting code here, each stirng value will need to be coverted to float
maxs = # add splitting code here 

dates = range(1,32)

plt.plot(dates, mins, dates, maxs) 
plt.show()
```

Modify the code to read the data from the marchweather.csv file – available on Blackboard. 
You should download it to your Prac5 directory, look at its contents and format, then modify 
the code accordingly. **Hint:** look at split method, and list comprehensions in lecture slides.

### Activity 2 - Reading another CSV file

This time, go to the Bureau of Meteorology site and download the full list of weather data for 
March. This time we will plot the min, max, 9am and 3pm temperatures... 
http://www.bom.gov.au/climate/dwo/202303/html/IDCJDW6111.202303.shtml

You can change the year and month by changing "202303" to another year+month

Save the data by scrolling down to the “Other Formats” section and right-clicking on the plain 
text version. Save it to your ```Prac05``` directory as ```marchweatherfull.csv```. If you open it in vim 
you can see all the data, but there are headers describing the data that we don’t need to read 
in. Remove the first header lines using ``dd`` (in vim's command mode) and then save the file. 
You now have your dataset.

Write a new program, ```marchweather2.py``` to read in the values and plot them. You will need 
to pick out columns from each line you read in from the file. First split it into a list, then 
pick out the values and assign them to the min, max, nine and three lists/arrays.

The code below will help start you off:
 
```python
fileobj = open(‘marchweatherfull.csv’, ‘r’) 
data = fileobj.readlines()
fileobj.close()

mins = [] # do the same for maxs, nines and threes

for line in data:
    splitline = line.split(‘,’) 
    mins.append(splitline[2]) 
    maxs.append(splitline[3]) 
    nines.append(splitline[10]) 
    threes.append(splitline[16])
```

Then adjust your ```plt.plot()``` call to plot mins, maxs, nines and threes. Make sure you 
set up the x values (dates) as in Task 1.

### Activity 3 - Writing to a CSV file
Take your marchweather2.py and modify it to write the four lists of values into a csv file, 
four values per line.
 
```python
file2 = open(‘marchout.csv’, ‘w’) 
for i in range(len(mins)):
    file2.write(mins[i] + ‘,’ + maxs[i] + ‘,’ + nines[i] + ‘,’ + threes[i] + ‘\n’)
file2.close()
```

### Activity 4 - List comprehensions

Using list comprehensions can reduce and simplify your code. In the lecture, we saw some 
examples of using list comprehensions. Using the lecture slides as a guide, write code to 
do the following using **both** loops and list comprehensions for each:

1. Make a list ```numbers``` with the numbers from 1 to 5
2. Write a function ```triple(n)``` and use it to triple each number in numbers
3. Write code to read in a string and extract all of the numbers (Hint: ```isdigit()```)
4. Write code to capitalise the first letter of each word in a list of words (Hint:you
can use use "+" to put the word back together)



### Activity 5 - Heat Diffusion

Download and run ```heat.py```, available in the practical area on Blackboard. There
have been some changes made over time to improve readability

```python
import numpy as np
import matplotlib.pyplot as plt

size = 20

currg = np.zeros((size,size))
print(currg)
for i in range(size):
    currg[i,0] = 10

nextg = np.zeros((size,size))

for timestep in range(5):
    for r in range(1, size-1):
        for c in range (1, size-1 ):
            ### HIGHLIGHTED CODE
            nextg[r,c] = (currg[r-1,c-1]*0.1 + currg[r-1,c]*0.1
                         + currg[r-1,c+1]*0.1 + currg[r,c-1]*0.1
                         + currg[r,c]*0.2 + currg[r,c+1]*0.1
                         + currg[r+1,c-1]*0.1 + currg[r+1,c]*0.1
                         + currg[r+1,c+1]*0.1)
            ### HIGHLIGHTED CODE
    for i in range(size):
        nextg[i,0] = 10
  
    print("Time step: ", timestep)
    print(nextg)
    currg = nextg.copy()
    
plt.imshow(currg, cmap=plt.cm.hot)
plt.show()
```

Make the following modifications to the code. The first improves readability, the
second gives the user more information about the progression of the heat diffusion.
Make sure you understand what the code does. Re-run the program after each change 
to see that it still works.

1. Modify the program to replace the highlighted code with the more readable code below:
```nextg[r,c] = 0.1 * (currg[r-1:r+2,c-1:c+2].sum() + currg[r,c])```
2. Modify the code to plot the current grid at the end of each timestep


### Activity 6 - Heat Diffusion with Functions

Our ```heat.py``` program has an ugly line of code to calculate the next values for each cell. 
We used an improved version, but hiding these ugly details in a function will make the code
more readable.

Copy ```heat.py``` to ```heatfun.py``` and create a function ```calcheat(subarray)``` to factor 
this calculation out. You can then call the function as:

```python 
            nextg[r,c] = calcheat(currg[r-1:r+2,c-1:c+2])
```
The lines to put in the function is:

``` python
def calcheat(subarray):
    result = 0.1 * (subarray.sum() + subarray[1,1])
    return result
```

### Activity 7 - Reading (yet another) CSV file

Copy your ```heat.py``` and call the copy ```heatsource.py```. This time we are going to read a heat source in from a file.

Create a file ```heatsource.csv to``` hold the heatsource:

(note, you can copy a line using ```yy``` and ```p``` in vim - *yank and paste*)
```
10,0,0,0,0,0,0,0,0,0
10,0,0,0,0,0,0,0,0,0
10,0,0,0,0,0,0,0,0,0
10,0,0,0,0,0,0,0,0,0 
10,0,0,0,0,0,0,0,0,0
10,0,0,0,0,0,0,0,0,0
10,0,0,0,0,0,0,0,0,0
10,0,0,0,0,0,0,0,0,0 
10,0,0,0,0,0,0,0,0,0
10,0,0,0,0,0,0,0,0,0
```

In our original program we had two loops to set up and maintain the heat source:

```
for i in range (size):
    currg[i,0]=10
```

This could also have been done in a more Pythonic way with:
```
currg[:,0] = 10
```

We are going to replace those lines with code to read the heat source from our 
file and update in each loop from our new h array to maintain the heat source.

Replace the first heat source code instance with the following to read data from a file:

```python
# create heat source
hlist = []
fileobj = open('heatsource.csv','r') 
for line in fileobj:
    line_s = line.strip()
    ints = [float(x) for x in line_s.split(',')] # list comprehension
    hlist.append(ints)
fileobj.close()

harray = np.array(hlist) 
currg = harray.copy()
```

And in the loop the heat source needs to be updated using the new h array...

```python
# Calculate heat diffusion 
for timestep in range(100):
    for r in range(1,size-1):
        for c in range (1, size-1):
            nextg[r,c]=calcheat(curr[r-1:r+2,c-1:c+2])

    for r in range(size):
        for c in range(size):
            if harray[r,c] > nextg[r,c]: 
                nextg[r,c] = harray[r,c]
    currg = nextg.copy()
```

Your code should now output the same information as it did before – test it and see.

In a similar way to list comprehensions, we can simplify the four lines of code above 
to one line using ```np.where()```. This will overwrite values in next where the value in 
harray is larger:

Copy ```heatsource.csv``` to  ```heatsource2.csv```, change the values in ```heatsource2.csv```,
and make the necessary changes to ```heatsource.py``` to see how it changes the output of the program.

### Activity 8 - Fireplan

Access the **Interactivate** app at: http://www.shodor.org/interactivate/activities/FireAssessment/

Explore the use of the app and how it is making use of the grid and neighbours. Also look 
at the use of graphics to represent the different states of a cell. What different graphics 
are used for the states and what do they represent?

### Activity 9 - Game of Life

Have a read of https://web.stanford.edu/class/sts129/Alife/html/Life.htm (a very old-school 
web page!) to see how the game of life works. 

Use your mouse to enter some life into the Game of Life Simulator https://playgameoflife.com/ , 
then click run to see the outcomes. How long does your population survive?

### Submission

Update the README file to include all files created in this practical.

All of your work for this week’s practical should be submitted via Blackboard using
the Practical 05 link. This should be done as a single "zipped" file.
Submit the resulting file through Blackboard. (refer to Practical 00 or 01 for instructions
on zipping files.
 
There are no direct marks for these submissions, but they may be taken into account 
when finalising your mark for the unit. Go to the Assessment link on Blackboard and 
click on Practical 03 for the submission page.

### And that's the end of Practical 05!

::::::::::::::::::::::::::::::::::::: keypoints 

- FIXME

:::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: checklist

### Reflection
 
1. **Knowledge:** What are the three different read methods we can use on a file? What is the difference between them?
3. **Comprehension**: What does the line file2.write(...) do in Activity 4?
5. **Application**: Given the Game of Life rules, what would happen to the centre
cell in the following cases:
![fig/P05GOLReviewQ.png](GOL images)
7. **Analysis**: What variation of “neighbours” does ```heatsource.py``` use? How would the code change if it were to use the other neighbour approach?
9. **Synthesis**: How would you create a heat source input file with a 4x4 heat source in the centre of the 10x10 grid?
10. **Evaluation**: Name two advantages to reading initial data from a file as in the updated ```heatsource.py```.
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: challenge

For those who want to explore a bit more of the topics covered in this practical. Note that the challenges are not assessed but may form part of the prac tests or exam.

1. Follow the workflow from Activity 3 to process and plot **February** weather data.
2. For students based in Australia, find another country's weather data sharing site, or an international one
If you are not in Australia, see if you can find you local government's weather data sharing site. 
4. Find and download some **Game of Life*** code and get it running.
 
::::::::::::::::::::::::::::::::::::::::::::::::
