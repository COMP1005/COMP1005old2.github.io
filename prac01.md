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
- Use Python to model simple systems

::::::::::::::::::::::::::::::::::::::::::::::::

### Introduction

In this practical you will continue to use Linux and the vim text editor - look back to [Practical 00](prac00.html)
to refresh yourself on those commands.

A With these skills, you can write your first few Python programs. In this case we will write 
a program to implement a simple systems dynamics model.

::::::::::::::::::::::::::::::::::::: challenge 

## Customising the mydesktop environment

You may prefer to have a black backgournd for your terminal, or to increase the time before the virtual machine goes to sleep... this will need to be done each time you use the virtual machines as they go back to the defaults every time.

:::::::::::::::::::::::: solution 

## Terminal window themes

There is a lot of customisation possible with the terminal window in Linux, but we will just look at "light" and "dark" themes. In the terminal menu, select edit/prefs.

[Changing preferences for theme 1/2](/episodes/P01pref.jpg){alt="Select edit/prefs in the terminal menu"}

Then choose 

![Changing preferences for theme 2/2](./episodes/P01theme.jpg){alt="Select dark then close"}

To go from dark to light...

![Changing preferences for theme 1/2](/episodes/P01pref_d.jpg){alt="Select edit/prefs in the terminal menu"}

Then choose 

![Changing preferences for theme 2/2](/P01theme_d.jpg){alt="Select dark then close"}

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::: solution 

## Changing the sleep settings

It may get annoying to keep putting the password in each time the virtual machine goes to sleep. The default timeout is 5 minutes, which can be increased to 15 minutes, or to "never". Select preferences and then Power at the top right of the Virtual Machine to change this setting.

![Changing preferences for timeout](/episodes/P01timeout.jpg){alt="Select preferences and then Power at the top right of the Virtual Machine"}

:::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::

![Changing preferences for theme 2/2](./P01theme_d.jpg){alt="Select dark then close"}


### Activity 1 - Setting up for the practical

We're going to make a complex directory structure for this practical. This will exercise 
your Linux skills for creating and traversing directories. The overall structure will be

```
FOP
 |-- Prac00
 |-- Prac01
   |-- The
   |   |-- Holy
   |   |   |-- Grail
   |   |
   |   |-- Life
   |       |-- of 
   |           |-- Brian
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

...or you can stay in the original directory and give the path to each new directory:

```
cd FOP/Prac01
mkdir The
mkdir The/Holy
mkdir The/Holy/Grail
```

To see the overall directory structure, type ```ls -R``` and you should have the output shown below:

![Output of ls -R on the Activity 1 directory structure](P01directories.jpg "Directory structure")

If you make a mistake, you can delete a directory with ```rmdir <dir_name```, but it must be empty first. Note that directories have to be empty before they can be deleted - so work from the "leaf" of the directory tree, back to the "root".

There are ways to delete a directory tree in one command, but it is too **dangerous** to teach at this point. For now, we'll do things the slow and safe way. 

::::::::::::::::::::::::::::::::::::: challenge 

## Challenge 1: Can you do it?

From the Prac01 directory, how would you cnange into the Grail directory **with one command**?

:::::::::::::::::::::::: solution 

## Solution

```output
cd The/Holy/Grail
```

:::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::

### Activity 2 - Interacting with Python Programs

Change directory to ```The/Holy/Grail```. We are going to write a program matching a scene from the movie "The holy Grail".

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

We can then ouptut these variables using print statements. 

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

There are many ways to solve a coding problem. Copy your code ```bridge.py``` to ```bridge2.py``` and then change the code to match the example below:

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

We always want to use the value collected in an ```input()``` call, so we can combine the ```print``` and ```input```
into a single line. Also, the ```print()``` calls can be absorbed into the strings being printed out, by 
including a ```\n``` to give a blank line. More on that in Lecture and Practical 2.

### Activity 3 - Control Structures (1a) if_elif_else (Bruce)
 
The previous code ran from the first line to the end, and will do so every time it runs. The if_elif_else
control structure can choose between different pieces of code. We need to put a Boolean condition into the 
```if``` or ```elif``` which Python will evaluate and choose a path through the code.

As an example, enter the following code, ```bruces.py```:

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

## Challenge 2: Testing, testing...

Looking at the above code, what inputs might you use to test it is working correctly?
:::::::::::::::::::::::: solution 

## Solution

Enter "Bruce" and something other than "Bruce" to test both paths through the code. Note that "Bruce" and "bruce" are not equal. 

:::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::

### Activity 4 - Control Structures (1b) if_elif_else (Guess who?)
 
To work through some more complex if_elif_else code, we'll identify the members of Monty Python:

- Graham Chapman - died 1989, cancer
- John Cleese - moustached
- Terry Gilliam - animator, bearded
- Eric Idle - composer, clean-shaven
- Terry Jones - died 2020, dementia
- Michael Palin - traveller, clean-shaven

The indenting indicates the start and end of each ``if_elif_else``` clause. Reducing the indent closes the clause, continuing the indent extends the included block. It can help to draw a ```flowchart``` to see/plan the flow of logic in your code.

```python
#
# whichone.py - asks questions to find your Python
#
print("\nFind the mystery Python!\n")
print("Enter Y/N to the following questions...")
male = input("Are you male? ")
if male != "Y":
    print("Not *technically* a python, however...")
    mystery = "Carole Cleveland"
else:
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
print("\nYour mystery Python is: ", mystery, "\n")
```

This one is a bit harder to test - see if you can get to every one of the Pythons.

### Activity 5 - Control Structures (2) while loops 
 
You now have a program and a README in the Prac00 directory. Enter the name of each of them
along with a description under “Contents” in the README file.

### Activity 6 - Making and submitting a zip file
 
This Practical includes a directory structure, so we will use a **recursive** option
on our zip command. To make a zipped file for Practical 01, go to FOP
directory. Type pwd to check that you are in the right place.
 
Create the zip file by typing:

```
zip -r Prac01_<your_student_ID> Prac01
 
e.g. zip -r Prac01_12345678 Prac01
```
 
This will create a file **Prac01_<your_student_ID>.zip** which includes
everything in the Prac01 directory – including the directories, programs and the README. You can check the
contents of the zip file by typing:

```
unzip –l Prac01_<your_student_ID>.zip
```
 
### Activity 8 - Submission

All of your work for this week’s practical should be submitted via Blackboard using
the Practical 01 link. This should be done as a single "zipped" file.
This is the file to submit through Blackboard. 
 
There are no direct marks for these
submissions, but they may be taken into account when finalising your mark.
Go to the Assessment link on Blackboard and click on Practical 0 for the submission
page.

### And that's the end of Practical 1!

::::::::::::::::::::::::::::::::::::: keypoints 

- input
- if_elif_else
- while loops
- for loops
- nesting control strucures

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: checklist

### Reflection
 
1. **Knowledge:** What are the three control structures we've learned?
2. **Comprehension:** What is the difference between the control structures?
3. **Application:** Give an example of where you might use each of the control structures?
4. **Analysis:** What variable would you change in growth.py to have more
iterations (steps) per hour?
5. **Synthesis:** How would you code a for loop to print “Hello World!” 15 times?
6. **Evaluation:** What part of the prac did you find most challenging? (You can
give feedback to the lecturer/tutor...)
 
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: challenge

For those who want to explore a bit more of the topics covered in this practical.

1. Have a look at other problems from the text book:
http://press.princeton.edu/titles/10291.html
2. Write a similar program to whichone.py, to determine a mystery animal/sport/food
3. How would growth.py change to be calculating compound interest?
 
::::::::::::::::::::::::::::::::::::::::::::::::
