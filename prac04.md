---
title: "Prac04: 2-Dimensional Arrays, Functions and Plotting"
---

:::::::::::::::::::::::::::::::::::::: questions 

- How can I work with data in two or more dimensions (x, y, z)?
- What are some examples of multi-dimensional data?
- How can I plot this multi-dimensional data?
- How do I make and use my own functions?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

1. Understand and use multi-dimensional arrays in Python using the Numpy library
2. Use sub-modules available the Scipy library
3. Define and use simple functions
4. Apply multi-dimensional arrays to multi-dimensional science data
5. Use matplotlib to plot multi-dimensional data


::::::::::::::::::::::::::::::::::::::::::::::::

### Introduction

In this practical you will be exploring the use 2-D arrays. We will use the ndimage sub-module of the Scipy package. Arrays are very useful for storing the values of variables representing areas. In heat.py we will look at a model for heat diffusion. In the final two exercises, we will work with functions, firstly on strings and then on the heat diffusion calculation.

### Activity 1 - Exploring 2-D Arrays

Type in the following code, zeros.py, for creating and resizing an array. Note that typing in the code helps you to learn python,
whereas copying and pasting code has no learning value.

```python
#
# zeros.py - creating and resizing an array 
#
import numpy as np
print('\nZERO ARRAY\n') 
zeroarray = np.zeros((3,3,3))

# update values here

print('Zero array size: ', np.size(zeroarray)) 
print('Zero array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)

zeroarray.resize((1,27))
print('\nZero array size: ', np.size(zeroarray)) 
print('Zero array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)

zeroarray.resize((3,9))
print('\nZero array size: ', np.size(zeroarray)) 
print('Zero array shape: ', np.shape(zeroarray), '\n')
print(zeroarray)
```

Modify the code to update the values. Set element ```[0,0,2]``` to 1, element ```[1,1,1]``` to 2 and ```[2,2,0]``` to 3. Run the code and note/understand where these values sit in each resized array.

### Activity 2 - Ndimage in Scipy

Type in the following code, prettyface.py – it’s from the lecture...
 
```python
#
# prettyface.py
#
import matplotlib.pyplot as plt 
from scipy import ndimage
from scipy import misc

face = misc.face(gray=True) 
plt.imshow(face)
plt.imshow(face, cmap=plt.cm.gray) 
plt.show()
```

Refer to the lecture slides and enter/run the code for shifting, rotating, cropping and pixelating.

Look at the documentation for colour maps and try a few of them with your code...
http://matplotlib.org/examples/color/colormaps_reference.html



### Activity 3 - Functions for Conversions

In this task we will create some functions to convert values between different units. To start, we will convert between 
Celsius, Fahrenheit and Kelvin. Below is a skeleton of how to start your code.

```python
#
# conversions.py – module with functions to convert between units #
# fahr2cel : Convert from Fahrenheit to Celsius.
#
def fahr2cel(fahr):
    """Convert from Fahrenheit to Celsius. Argument:
    fahr – the temperature in Fahrenheit """
    celsius = (fahr – 32) * (5/9) 
    return celsius
```

Note that we are using docstrings to document our functions. See the related PEP for more about docstrings - https://www.python.org/dev/peps/pep-0257/

Write some test code to test out your functions. You could start with something like the code below, or work with user input.

```python
#
# testConversions.py - tests the functions in conversions.py 
#
from conversions import *
print("\nTESTING CONVERSIONS\n")
testF = 100
testC = fahr2cel(testF)
print("Fahrenheit is ", testF, " Celsius is ", testC)
print()
```

Extend conversions.py to include all six conversion functions, along with others you might find useful. Extend your test program to test the other conversions.
To see the docstring for a function, you access the ```__doc__``` attribute. So to print the docstring for fahr2cel, you could use: ```print(fahr2cel.__doc__)```. This
is how the IDE's access the information to give you help with usage as you type in a function. 


### Activity 4 - Conversion Machine (1)

Now we can write a program, ```converter.py```, to convert between our temperature formats. Your program should:

1. print starting message
2. provide a menu of conversions to choose between
3. take the user input
4. while the choice is to keep going
   1. do the conversion, or provide an error message
   2. ask if they want to do another conversion
   3. loop back to (4) 
8. print closing message

This is very similar to the Bucket List Builder, so refer to Practical 02 to see that code.


### Activity 5 - Conversion Machine (2)

Create a different version of the conversion machine, converter2.py, that will ask for the 
conversion type, then will convert a list of numbers into the target unit. The loop should 
exit when the user enters an empty value (just presses return).

1. print starting message
2. provide a menu of conversions to choose between
3. take the user input
4. while the choice isn't an empty string
   5. do the conversion, or provide an error message
   6. ask if they want to do another conversion
   7. loop back to (4) 
8. print closing message


### Activity 6 - Conversion Machine (3)

Think about the input you are giving to ```converter2.py```. Could you automate that input?

We can redirect input in the same way that we redirected the output of history in the practical 
test (```history > hist.txt```). Create a file ```temps.txt``` with sample input for your ```converter2.py```
program, then try:

```
python3 converter2.py < temps.txt
```

To capture the results, you can also redirect the output:

```
python3 converter2.py < temps.txt > tempsout.txt
```

Make a larger input file to see how easy it is to process data using **standard in** (keyboard input) and **standard out** (screen output).

### Activity 7 - Testing your Module

In the lecture (slide 71), we saw how we can use the ```__main__``` attribute/variable 
to check if our python code has been run directly (e.g. ```python3 conversions.py```) or indirectly 
(e.g. ```from conversions import *, temp = fahr2cel(100))```. Using this, we can create test 
code inside our module.

Modify ```conversions.py``` to include test code by implementing a ```main()``` function and putting the required if statement at the end of the module.
Test your changes by running the conversions.py from the command line.

```python3 conversions.py```

The additional code for ```conversions.py``` is:

```python 
def main():
    print('\nTesting textfun.py ')
    # put your testing code in here
    print('Testing complete')

if __name__ == '__main__':
    main()
```

### Activity 8 - Specifications and Pseudocode
The lecture slides included a description and pseudocode specification of a program for collecting gymnastics competition scores.

Translate the first version of the program to python (call it ```competition_v1.py```) and test it to check how it 
handles invalid data, and the impact of the dodgy data on the results (e.g. score of -100).

Make a copy of the code as ```competition_v2.py``` and adjust it to match the second version of the 
pseudocode from the slides. Test it again with bad input to see how it is handled.

Finally make another copy ```competition_v3.py``` and modify it to match version three from the lecture 
slides. Try the same tests to check it is working correctly.


### Submission

Create a README file for Prac 04. Include the names and descriptions of all of your Python programs from this practical.

All of your work for this week’s practical should be submitted via Blackboard using the link under assessments. This 
should be done as a single "zipped" file. A reminder that these are not assessed, but we may look at the submission of practicals as an indicator of your engagement and effort in the unit.

### And that's the end of Practical 04!

::::::::::::::::::::::::::::::::::::: keypoints 

* Numpy provides multi-dimensional arrays in Python, along with useful functions and operations
* Indexing and slicing are used in a similar way to other sequences (1-D arrays, strings and lists)
* The Scipy library extends Numpy with more advanced functionality, including image processing. Images can be manipulated as Numpy arrays.
* We can improve readibility and reduce repetition by defining and using functions.
* Once a function has been **tested** - it can be used with confidence, which simplifies your code.
* Functions can be grouped into modules and imported and reused in multiple programs


:::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: checklist

### Reflection
 
1. **Knowledge:** What are three benefits of using functions?
3. **Comprehension**: What is the purpose of the ```colourmap(cmap=    )``` in Task2?
5. **Application**: How would you change the plot of the critter to be shades of purple and in reverse? (like a negative of a photo)
7. **Analysis**: Task 7 uses the Python variable ```__name__``` to support testing. What does ```__name__``` equal when the module code is run directly (as ```python conversions.py```), and what is its value when the module is run as ```python converter2.py```?
9. **Synthesis**: What happens when we resize an array to be smaller than the original? What happens when we make it larger? Does the data in the array change?
10. **Evaluation**: Compare the three versions of the competition code from task 3. How has the code improved from 
  * the user perspective, and
  * the programmer perspective.
 
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: challenge

For those who want to explore a bit more of the topics covered in this practical. Note that the challenges are not 
assessed but may form part of the prac tests or exam.

1. Create a program to convert an inputted string to Pig Latin
2. Find a repetitive song and use functions e.g. ```print_lyrics()``` to print out the complete song. Examples include:
  * 10 Green Bottles
  * 5 Little Ducks
  * Bingo
    
::::::::::::::::::::::::::::::::::::::::::::::::
