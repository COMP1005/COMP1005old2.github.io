---
title: "Prac02: Strings and Lists"
---

:::::::::::::::::::::::::::::::::::::: questions 

- How do I work with string values and variables?
- How do I access the elements of strings and lists?
- How can I use random numbers to simulate real world situations?
 
::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

1. Define and use more complex datatypes (strings and lists) and variations on control structures
2. Use slicing and indexing to access elements in a list
3. Use a supplied Python package to provide random number options
4. Understand and implement simple Monte Carlo algorithms

::::::::::::::::::::::::::::::::::::::::::::::::

### Introduction

In this practical we will enter and modify programs to work with and explore strings and lists. We will then use random numbers to select list items without replacement.
The final two tasks will implement two Monte Carlo algorithms: calculating Pi and tossing coins.

### Activity 1 - Setting up for the practical

Login to the computers as in Practical 1. Within your home directory (/home/student_id) you should have the following structure:

```
FOP
 |-- Prac00
 |-- Prac01
 |-- Prac02
 |-- Prac03
 |-- Prac04
 |-- Prac05
 |-- Prac06
 |-- Prac07
 |-- Prac08
 |-- Prac09
 |-- Prac10
 |-- Prac11
```

Type ```ls FOP``` from your home directory to check your directory structure.

We will be working in the ```Prac02``` directory today. If you do not have the directory
structure correct, your tutor can help you to rearrange it.

Copy the ```README``` file from your ```Prac01``` directory to your ```Prac02``` directory. Use
```cp ../Prac01/README .``` from within the ```Prac02``` directory, then ```vim README``` to edit. 
Update the ```README``` to refer to ```Prac02``` and include the correct date.


### Activity 2 - Everybody loves string(s)!

Strings are very important in Python and the language provides powerful options to manipulate 
strings. The code below shows three different approaches to printing out a string in reverse: 
**while** loops; **for** loops and using **slicing**. 

Enter the foloowing code as ```strings1.py```...

```
#
# strings1.py: Read in a string and print it in reverse
#              using a loop and a method call

instring = input('Enter a string... ')

# *** add (2) upper and (3) duplicating code here

# reversing with a while loop
print('Reversed string is : ', end='')
index = len(instring)-1
while index > -1:
    print(instring[index], end='')
    index = index - 1
print()

# reversing with a for-range loop
print('Reversed string is : ', end='')
for index in range(len(instring)-1, -1, -1):
    print(instring[index], end='')
print()

# reversing with slicing
print('Reversed string is :', instring[len(instring)-1:-1:-1])
```

Test out the code to understand how it works. Note that in each case:

- **start** value is ```len(instring)-1```
- **stop** value is ```-1```
- **step** value is ```-1```

Next, copy ```strings1.py``` to ```strings2.py``` and make the following changes...

1. Change the **start**, **stop** and **step** values in each approach to print the string forwards (instead of in reverse).
2. Update instring to uppercase (so that ‘abcd’ becomes ‘ABCD’)
3. Update instring to duplicate the string (ABCD becomes ABCDABCD)
4. Modify each of the three approaches print out every second character (ABCDABCD becomes ACAC)
5. Modify each of the three approaches print out every second character, excluding the first and last (ABCDABCD becomes
BDB)

### Activity 3 - Bucket List

The Bucket List is a movie from 2007 where two men work through a list of things they want to do in life. This task will have you work with their bucket list.
You will define bucket1 directly as a list, then append three values. Deleting a value uses the index of the item in the list (e.g. del bucket1[5] ) We then create a second list and make a new list bucket fomr bucket1 + bucket2. Finally we insert a new item and print out the buckets.
 
#
# bucket1.py - use a python list for items in a bucket list
#
print('\nBUCKET LIST\n')
bucket1 = ['Witness something truly majestic',
          'Help a complete stranger',
          'Laugh until I cry','Drive a Shelby Mustang']
bucket1.append('Kiss the most beautiful girl in the world')
bucket1.append('Get a tattoo')
bucket1.append('Skydiving')
del bucket1[5]
bucket2 = ['Visit Stonehenge',
           'Drive a motorcycle on the Great Wall of China',
           'Go on a Safari','Visit the Taj Mahal',
           'Sit on the Great Egyptian Pyramids',
           'Find the Joy in your life']
print('Bucket 1: ', bucket1)
print('Bucket 2: ', bucket2)
bucket = bucket1 + bucket2
bucket.insert(5, 'Get a tattoo')
print('Joined buckets: ', bucket)
print('\nNicer formatting....\n')
for item in bucket:
    print(item)
We will now create a bucket list builder to interactively create a new bucket list...
 
#
# bucket2.py - bucket list builder
#
print('\nBUCKET LIST BUILDER\n')
bucket = []
choice = input('Enter selection: e(X)it, (A)dd, (L)ist...')
while choice[0] != 'X':
    if choice[0] == 'A':
        print('Enter list item... ')
        newitem = input()
        bucket.append(newitem)
    elif choice[0] == 'L':
        for item in bucket:
print(item)
    else:
        print('Invalid selection.')
    choice = input('Enter selection: e(X)it, (A)dd, (L)ist..')
print('\nGOODBYE!\n')
 Modify the code to:
1. Acceptlowercaseaswellasuppercaselettersaschoices(hint:upper())
2. Provideanoptionfordeletingitems(hint:delbucket[int(delitem)])

### Activity 4 - Control Structures: if_elif_else + nesting
 
To work through some more complex if_elif_else code, we'll write a program to identify the members of Monty Python:

| Name           | Description | 
|----------------|-------------|
| Graham Chapman | died 1989, cancer |
| John Cleese    | not dead yet, moustached |
| Terry Gilliam  | animator, not dead yet, bearded |
| Eric Idle      | composer, not dead yet, clean-shaven |
| Terry Jones    | died 2020, dementia |
| Michael Palin  | not dead yet, traveller, clean-shaven |


For this exercise, enter your code as ```which.py``` in the ```Monty/Pythons``` directory. Indenting must be correct for this code to work! It can help to draw a ```flowchart``` to see/plan the flow of logic in your code.

```python
#
# which.py - asks questions to find your Python
#
print("\nFind the mystery Python!\n")
print("Enter Y/N to the following questions...")
male = input("Are you male? ")
if male == "Y":
    beard = input("Do you have a beard? ")
    if beard == "Y":
        mystery = "Terry Gilliam"
    else:
        alive = input("Are you still alive? ")
        if alive != "Y":
            dementia = input("Did you have dementia? ")
            if dementia == "Y":
                mystery = "Terry Jones"
            else:
                mystery = "Graham Chapman"
        else:
            mo = input("Do you have a moustache? ")
            traveller = input("Are you a traveller? ")
            if mo == "Y":
                mystery = "John Cleese"
            elif traveller == "Y":
                mystery = "Michael Palin"
            else:
                mystery = "Eric Idle"
else:
    print("Not *technically* a python, however...")
    mystery = "Carole Cleveland"
print("\nYour mystery Python is: ", mystery, "\n")
```

This one is a bit harder to test - see if you can get to every one of the Pythons.

### Activity 5 - Control Structures: For loops 
 
When we take input from the user, it is read in as a string. These are characters - so we need to 
convert them to actually use them as numbers. The following code demonstrates this conversion.

Type it in as ```num_convert.py``` in the ```Prac01``` directory.

```python
#
# num_convert.py: Read in number and convert to int and float
#
print('Enter a number...')
numstr = input()
print('Number =', numstr, ' Type : ', str(type(numstr)))
numint = int(numstr)
print('Number =', numint, ' Type : ', str(type(numint)))
numfloat = float(numstr)
print('Number =', numfloat, ' Type : ', str(type(numfloat)))
```

Notice how the first two print statements print the same number (well, it looks the same), 
but their variable types are different? Everything you read in will be a string. If 
you want a number, you'll need to convert it with the int() or float() functions.

Testing this code will show you some easy ways to break a program. We'll learn later how to make the code more robust 
(spoiler - it's exception handling).

Now we are going to read in ten numbers and add up their total. As we know in advance how many 
of numbers we want, we can use a ```for`` loop. Type it in as ```num_for.py``` in the ```Prac01``` directory.
 
```python
#
# num_for.py: Read in ten numbers and give sum of numbers 
#
print('Enter ten numbers...')
total = 0
 
for i in range(10):
    print('Enter a number (', i, ')...')
    number = int(input())
    total = total + number
print('Total is ', total)
```
 
Save and exit the file and try running it. What are the values that variable "i" holds each time 
through the loop? How would you change the for loop in the program to request five numbers be entered.

These ```for``` loops will **start** at zero and go up to, but not including, the **stop** value. 

- ```for i in range(10):``` will give us ```i = 0,1,2,3,4,5,6,7,8,9```
- ```for i in range(5):``` will give us ```i = 0,1,2,3,4```
- ```for i in range(1,6):``` will give us ```i = 1,2,3,4,5```

### Activity 6 - Control Structures: While loops 

Sometimes we don't know how many loops we want to make, but we will know when we get there - we can 
test a condition (similar to an ```if``` control structure). In this code we will enter numbers, and 
type in a negative number to exit the loop. This is called a **sentinel value**.

Type it in as ```num_while.py``` in the ```Prac01``` directory.

```
#
# num_while.py: Read in a list of numbers (negative to exit) and
#               give the sum of the numbers
count = 0
total = 0
print("Enter a list of numbers, negative to exit...")
number = int(input())
while number >= 0:
    count += 1           # equivalent to count = count + 1
    total += number      # equivalent to total = total + number
    print("Next number...")
    number = int(input())
print("Total is ", total, " and count is ", count)
```

Save and exit and then run ```num_while.py```. 

:::::: challenge

How would you need to change the while loop in the code to have it exit on **zero** instead of negative numbers?

::::: solution

```
while number != 0:
```

:::::

::::::

### Activity 7 - And Now For Something Completely Different 
 
Now for a simple systems model... Unconstrained Growth and Decay.

::::: callout

## From the "Introduction to Computational Science" text:

*“Many situations exist where the rate at which an amount is changing is proportional to the amount present. Such might be the case for a population, say of people, deer, or bacteria. When money is compounded continuously, the rate of change of the amount is also proportional to the amount present. For a radioactive element, the amount of radioactivity decays at a rate proportional to the amount present.”*

:::::

So, growth and decay models are common in many domains. We will implement algorithm 2 from Module 2.2 of the text book (p25). 
Chapter 2 is available for download at [Computational Science](http://press.princeton.edu/titles/10291.html), and 
provides background to these types of models.

We are going to write Python code for simulating unconstrained growth based on the following pseudocode from the text:
 
::::: callout

## Algorithm 2 - simulation of unconstrained growth

- initialise simulation length
- initialise population
- initialise growth rate
- initialise (length of) time step
- number of iterations = simulation length / time step growth rate (per step) = growth rate * time step
- for i = 0 to number of iterations-1 do
   - growth = growth rate (per step) * population population = population + growth
   - time = i * time step
   - display time, growth, population

:::::

Compare this to the following code. We are implementing the scenario which follows the Algorithm on page 25.

Enter the code as ```growth.py``` in the ```And/Now/for/Something/Completely/Different``` directory.

```python
#
# growth.py - simulation of unconstrained growth
#
print("\nSIMULATION - Unconstrained Growth\n")
length = 10
population = 100
growth_rate = 0.1
time_step = 0.5
num_iter = length / time_step
growth_step = growth_rate * time_step
print("INITIAL VALUES:\n")
print("Simulation Length (hours): ", length)
print("Initial Population: ", population)
print("Growth Rate (per hour): ", growth_rate)
print("Time Step (part hour per step): ", time_step)
print("Num iterations (sim length * time step per hour): ",
num_iter)
print("Growth step (growth rate per time step): ",
growth_step)
print("\nRESULTS:\n")
print("Time: ", 0, " \tGrowth: ", 0, " \tPopulation: ", 100)
for i in range(1, int(num_iter) + 1 ):
    growth = growth_step * population
    population = population + growth
    time = i * time_step
    print("Time: ", time, " \tGrowth: ", growth, "\tPopulation: ", population)
print("\nPROCESSING COMPLETE.\n")
```

Type in the code and run it. 

:::::: challenge

Can you see why the for loop was changed from ```0``` to ```num_iter``` to ```1``` to ```num_iter+1```?

::::: solution

Time step 0 is the initial step, before the loop. Our loop will go through num_iter times, starting at one. 
Loops usually go from 0 to maximum-1 to have maximum iterations. If we shift the start up by 1, we also have to 
shift the stop value by 1.

:::::

::::::


### Activity 8 - Making and submitting a zip file
 
This Practical includes a directory structure, so we will use a **recursive** option
on our zip command. To make a zipped file for Practical 01, go to FOP
directory. Type pwd to check that you are in the right place.
 
Create the zip file by typing:

```
zip -r Prac01_<your_student_ID> Prac01
 
e.g. zip -r Prac01_12345678 Prac01
```
 
This will create a file **Prac01_<your_student_ID>.zip** which includes
everything in the Prac01 directory – including the directories, programs 
and the README. As before, you can check the contents of the zip file by typing:

```
unzip –l Prac01_<your_student_ID>.zip
```
 
### Submission

All of your work for this week’s practical should be submitted via Blackboard using
the Practical 01 link. This should be done as a single "zipped" file.
This is the file to submit through Blackboard. 
 
There are no direct marks for these
submissions, but they may be taken into account when finalising your mark.
Go to the Assessment link on Blackboard and click on Practical 0 for the submission
page.

### And that's the end of Practical 01!

::::::::::::::::::::::::::::::::::::: keypoints 

- We use ```input()``` to get the user's input from the keyboard, and ```print()``` to output to the screen
- To choose between parts of the code to run, we can use the ```if_elif_else``` control structure
- If we want to repeat code, we can use ```for loops``` and ```while loops```
- ```while loops``` continue until a condition is false - we don't know at the start how many times they will run
- ```for loops``` repeat a set number of times, so we should use them when we know how many iterations we want
- We can **nest** control strucures by indenting them inside each other

:::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: checklist

### Reflection
 
1. **Knowledge:** What are the three control structures we've learned?
2. **Comprehension:** What is the difference between the control structures?
3. **Application:** Give an example of where you might use each of the control structures?
4. **Analysis:** What variable would you change in growth.py to have more iterations (steps) per hour?
5. **Synthesis:** How would you code a for loop to print “Hello World!” 15 times?
6. **Evaluation:** What part of the prac did you find most challenging? (You can give feedback to the lecturer/tutor...)
 
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: challenge

For those who want to explore a bit more of the topics covered in this practical.

1. Have a look at other problems from the text book:
http://press.princeton.edu/titles/10291.html
2. Write a similar program to whichone.py, to determine a mystery animal/sport/food
3. How would growth.py change to be calculating compound interest?
 
::::::::::::::::::::::::::::::::::::::::::::::::
