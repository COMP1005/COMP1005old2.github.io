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

Run the program a few times to see how it works. The ```input()``` call puts up a prompt for the user to enter text on the keyboard. To store the input in a variable, we assign in using an "=" sign: ```name = input()```. We do similar for the quest and favourite colour.

We can then ouptut these variables using print statements. 

Once you have that working, we can improve on the code and make it a bit friendlier. Edit the code again and make the 
changes below:

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

### Activity 3 - Introduction to the Text Editor (vim)
 
We are going to use the vim text editor to create your README file for Prac01. Vim
is an enhanced version of vi – a visual, interactive editor. There is an Introduction to
Vi document and a “cheat-sheet” on Blackboard, but you should work through this prac before 
try ing it.
 
If you're not already there, change directory into the Prac00 directory and create the README file:

```
> cd Prac00
> vim README
```
 
You will now be in the vim text editor with an empty file. Vim has two modes –
command mode (where you can move around the file and use commands) and insert
text mode. Type “i” to go into insert mode and type in the following README
information for Practical 1.
 
```
## Synopsis
Practical 0 of Fundamentals of Programming COMP1005/5005
 
## Contents
README – readme file for Practical 0
 
## Dependencies
none
 
## Version information
<today’s date> - initial version of Practical 0 programs
```
 
Press ```<esc>``` to exit insert mode, then :wq to save the file (w) and exit vim (q).
Type:

```
ls -l
```
 
(-l for long listing) and you will see that you have created a file called README, and it has
a size and a date. We will make README files for all of our practicals to hold
information about the files in that directory.

### Activity 4 - Welcome to Python!
 
Below is a simple program to get you used to the editor and running python scripts.
To create a file for the program, type:
 
```
vim hello.py
```
 
Then type in the following code... It is important to type it yourself and not copy/paste
– this is how you will learn and remember!

```python
#
# hello.py: Print out greetings in various languages
#
print('Hello')
print("G'day")
print('Bula')
print("Kia ora")
```

To run the program, type:
 
```
python3 hello.py
```
 
You will probably get an error message as a response (unless you typed it in
perfectly). Don’t worry, check through your code for the error and try running it again.
Go back into the file and make corrections – use the cursor keys to get to the position
(<lineno>G). Some handy editing commands are:
 
* to delete a character type “x”
* to delete a line “dd”
* to delete a word “dw”
* to change a word “cw”
* to insert/append after the end of the current line, type “A”
* to undo the last command, type “u”
* to redo the last command, type “.”

Save the file and try to run it again. If you’re having trouble, ask your tutor, or even
the person next to you, to see if they can find what’s wrong. Sometimes it takes
someone else’s fresh and/or experienced eyes to see an error. This is called
“debugging” and the reward comes when the code finally runs!

Try adding some more greetings of your own...

 
### Activity 5 - Updating the README
 
You now have a program and a README in the Prac00 directory. Enter the name of each of them
along with a description under “Contents” in the README file.

### Activity 6 - Making and submitting a zip file
 
To bundle up and compress files we can use zip/unzip. Similar programs are tar
(Tape Archive) and gzip (GNU zip).
 
To make a zipped file for Practical 0, go to the Prac00 directory inside your FOP
directory. Type pwd to check that you are in the right place.
 
Create the zip file by typing:

```
zip Prac00_<your_student_ID> *
 
e.g. zip Prac00_12345678 *
```
 
This will create a file **Prac00_<your_student_ID>.zip** which includes
everything in your current directory – four programs and the README. You can check the
contents of the zip file by typing:

```
unzip –l Prac00_<your_student_ID>.zip
```
 
### Activity 7 - Submission

All of your work for this week’s practical should be submitted via Blackboard using
the Practical 0 link. This should be done as a single "zipped" file.
This is the file to submit through Blackboard. 
 
There are no direct marks for these
submissions, but they may be taken into account when finalising your mark.
Go to the Assessment link on Blackboard and click on Practical 0 for the submission
page.

### And that's the end of Practical 0!

::::::::::::::::::::::::::::::::::::: keypoints 

- We will be using Linux as our operating system for this unit
- You can access Linux through [mydesktop.curtin.edu.au](https://mydesktop.curtin.edu.au) or install Python and a "Linux" shell on your home machine
- Working on the command line, we will type in commands at the prompt, press enter, and wait for the computer's response
- To create and edit a text file, we will be using vim - a program for editing text files
- Once we have entered a Python program as a text file, with a ".py" extension, we can run the program by typing `python3 myprog.py`

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: checklist

### Reflection
 
1. **Knowledge:** What are the two modes in vi / vim?
2. **Comprehension:** What is the name of the lab machine you are working on?
Hint: use the hostname command or look at the prompt.
3. **Application:** What series of commands would you need to go to the directory
FOP/assignment in your home directory and compress all the files?
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
2. Work through a Linux tutorial
3. Work through a vi/vim tutorial
4. Read some samples of README files for large projects -
https://github.com/matiassingers/awesome-readme
 
::::::::::::::::::::::::::::::::::::::::::::::::
