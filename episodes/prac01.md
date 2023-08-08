---
title: "Prac01: Introduction to Python"
---

:::::::::::::::::::::::::::::::::::::: questions 

- How do I interact with a Python program?
- How can I get Python to run different pieces of code, based on a condition?
- What ways can I have Python repeat code?
- How do I apply this to a real-world problem?
 
::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

- Continue to use key commands in the Linux operating system
- Request user input in Python
- Create and work with variables and values of different types
- Define and use control structures
- Use Python to model a simple system

::::::::::::::::::::::::::::::::::::::::::::::::

### Introduction

In this practical you will continue to use Linux and the vim text editor - look back to [Practical 00](prac00.html)
to refresh yourself on those commands. The first activity sets up the directory structure for the practical.

We will be looking at accepting user input (Activity 2) and control structures (Activities 3-6). In Activity 7 
we will write a program to implement a simple systems dynamics model.

### Activity 1 - Setting up for the practical

We're going to make a more complex directory structure for this practical. This will exercise 
your Linux skills for creating and traversing directories. The overall structure will be:

```
FOP
 |-- Prac00
 |-- Prac01
   |
   |-- The
   |   |-- Holy
   |   |   |-- Grail
   |
   |-- Monty
   |   |-- Pythons
   |       |-- Flying 
   |           |-- Circus
   |-- And
       |-- Now
           |-- for 
               |-- Something
                   |-- Completely
                       |-- Different
```

Each indent is a subdirectory. You might create each directory, then ```cd``` into it, then create the subdirectory:

```
cd FOP/Prac01
mkdir The
cd The
mkdir Holy
cd Holy
mkdir Grail
cd ../..
```

Or you can stay in the original directory and give the path to each new directory:

```
cd FOP/Prac01
mkdir The
mkdir The/Holy
mkdir The/Holy/Grail
```

To see the overall directory structure, type ```ls -R``` and you should have the output shown below:

![Output of ls -R on the Activity 1 directory structure](fig/P01directories.png "Directory structure")

If you make a mistake, you can delete a directory with ```rmdir <dir_name>```. Note that directories have to be empty before they can be deleted - so work from the "leaf" of the directory tree, back to the "root".

There are ways to delete a directory tree in one command, but it is too **dangerous** to teach at this point. For now, we'll do things the slow and safe way. 

::::::::::::::::::::::::::::::::::::: challenge 

## Challenge 1: Can you do it?

From the Prac01 directory, how would you change into the Grail directory **with one command**?

:::::::::::::::::::::::: solution 

## Solution

```
cd The/Holy/Grail
```

:::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::

### Activity 2 - Interacting with Python Programs

Change directory to ```The/Holy/Grail```. We are going to write a program matching a scene from the movie "The Holy Grail".

In the Grail directory, type in:

```vim bridge.py```

then type in the following code:

```python
#
# bridge.py - a scene from The Holy Grail
#
print("Welcome to the Bridge of Death")
print("What is your name?")
name = input()
print("What is your quest?")
quest = input()
print("What is your favourite colour?")
colour = input()
print(name)
print(quest)
print(colour)
```

Run the program a few times to see how it works. The ```input()``` call puts up a 
prompt for the user to enter text on the keyboard. To store the input in a variable, 
we assign in using an "=" sign: ```name = input()```. We do similar for the quest 
and favourite colour.

We can then output these variables using print statements. 

Have you noticed that the code changes colour as you type? This is syntax highlighting. When you’re 
in command mode in vim you can type ```:syntax off``` and ```:syntax on``` to turn it off/on.

Once you have that working, we can improve on the code and make it a bit friendlier. 
Edit the code again and make the changes below:

```python
#
# bridge.py - a scene from The Holy Grail
#
print()
print("Welcome to the Bridge of Death")
print()
print("What is your name?")
name = input()
print("What is your quest?")
quest = input()
print("What is your favourite colour?")
colour = input()
print()
print("Hello,", name, "good luck with your", quest, "quest!")
print("Perhaps wearing", colour, "socks would help :)")
print()
```

There are many ways to solve a coding problem. Copy your code ```bridge.py``` to ```bridge2.py``` and then change the code to match the example below. The required commands are:

```
cp bridge.py bridge2.py
vim bridge2.py
```

```python
#
# bridge2.py - a scene from The Holy Grail, re-coded
#
print("\nWelcome to the Bridge of Death\n")
name = input("What is your name?")
quest = input("What is your quest?")
colour = input("What is your favourite colour?")
print("\nHello,", name, "good luck with your", quest, "quest!")
print("Perhaps wearing", colour, "socks would help :)\n")
```

We always want to make use of the value collected in an ```input()``` call, so we can combine the ```print``` and ```input```
into a single line. Also, the empty ```print()``` calls can be absorbed into the strings being printed out, by 
including a ```\n``` to give a blank line. More on that in Lecture and Practical 2.

### Activity 3 - Control Structures: if_else
 
The previous code ran from the first line to the end, executing every line, 
and will do so every time it runs. The ```if_elif_else```
control structure allows us to choose between different pieces of code to run. We just need to put a Boolean 
condition (```True/False```) into the ```if``` or ```elif``` and Python will evaluate it and choose a path through the code.

The indenting indicates the start and end of each ```if_elif_else``` clause. Reducing the indent 
closes the clause, continuing the indent extends the included block. 

As an example, enter the following code, ```bruces.py```, in the directory ```Monty/Pythons/Flying/Circus```:

```python
#
# bruces.py - let's call everyone "Bruce", to avoid confusion
#
name = input("\nHey cobber, what's your name? ")
if name != "Bruce":
   print("Sorry,", name,"- your name's not Bruce?")
   print("That's goin to cause a little confusion.")
   print("Mind if we call you 'Bruce' to keep it clear?")
   name = "Bruce"
print("G'day", name, "!!!\n")
```

We can enhance the program to congratulate anyone who is actually called Bruce... update the code as below.

```python
#
# bruces.py - let's call everyone "Bruce", to avoid confusion
#
name = input("What is your name? ")
if name != "Bruce":
   print("Sorry,", name,"- your name's not Bruce?")
   print("That's going to cause a little confusion.")
   print("Mind if we call you 'Bruce' to keep it clear?")
   name = "Bruce"
else:
   print("Excellent! That saves a lot of confusion!")
print("G'day", name)
```

::::::::::::::::::::::::::::::::::::: challenge 

## Challenge 2: Testing... testing...

Looking at the above code, what inputs might you use to test it is working correctly?

:::::::::::::::::::::::: solution 

## Solution

Enter "Bruce" **and then** something other than "Bruce" to test both paths through the code. 
Note that "Bruce" and "bruce" are not equal. Testing requires at least every path through the code is executed.

::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::

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
of numbers we want, we can use a ```for``` loop. Type it in as ```num_for.py``` in the ```Prac01``` directory.
 
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
Chapter 2 is available for download at [Computational Science](files/s2_10291.pdf), and 
provides background to these types of models.

We are going to write Python code for simulating unconstrained growth based on the following pseudocode from the text:
 
::::: callout

## Algorithm 2 - simulation of unconstrained growth

- initialise simulation length
- initialise population
- initialise growth rate
- initialise (length of) time step
- number of iterations = simulation length / time step
- growth rate (per step) = growth rate * time step
- for i = 0 to number of iterations-1 do
   - growth = growth rate (per step) * population
   - population = population + growth
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
and the README. 

As before, you can check (list) the contents of the zip file by typing:

```
unzip –l Prac01_<your_student_ID>.zip
```
To unzip the file, just do the above command without the ```-l```

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
