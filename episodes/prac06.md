---
title: "Prac06: Modelling the World with Objects"
---

:::::::::::::::::::::::::::::::::::::: questions 

- How can we set up classes to represent real-world objects?
- How do we write methods to communicate with our objects?
- How can our code help to maintain a valid state in the object?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

1. Understand the main concepts in object- oriented programming and their value
2. Read and explain object-oriented code
3. Apply and create simple object-oriented Python code

::::::::::::::::::::::::::::::::::::::::::::::::

### Introduction

In this practical you will write Python programs to implement the objects 
used as examples in the lecture. We will see how to create and manipulate 
objects, and how to group them in useful ways.

### Activity 1 - Animals as Objects

We will keep our class definitions in separate python files. In your 
Practical 6 directory, edit ```animals.py``` with vim. Enter the class definition for ```Cat``` into ```animals.py```.

If you try to run ```animals.py```, what happens?

We need a driver program to test out our ```Cat``` class. Edit ```testCat.py``` and enter the following code:

```python
from animals import Cat

garfield = Cat(‘Garfield’, ‘1/1/1978’, ‘Orange’, ‘Tabby’)

garfield.printit()

print(garfield)
```

Note the difference in the output of ```garfield.printit()``` and ```print(garfield)```.

### Activity 2. More Animals!

Edit animals.py and add in the class definitions for Dog and Bird. Create some test 
data and code in testAnimals.py to test all three classes. Use testCat.py and the 
lecture notes as a starting point.

### Activity 3 - Even more animals!

Following the general outline for our programs, we will now create a program to read 
in animals from a file into a list of animal objects. The file will hold comma-separated 
values. Our algorithm will be:

1. Openfile
1. Read data from file into animal list
2. Print animal list using printit() method

More detail of what we will need in our code is:

1. Import classes 
2. Create variables 
3. Open file 
  - For each line in the file
  - Create animal object using class matching first field in the entry 
  - Add it to the animal list
6. Print animal list

Have a look at ```animals.csv``` (below) to see how you can read in the file.

```
Dog,Dude,1/1/2011,Brown,Jack Russell 
Cat,Oogie,1/1/2006,Grey,Fluffy 
Bird,Big Bird,10/11/1969,Yellow,Canary 
Cat,Garfield,1/1/1978,Orange,Tabby
```

Work through each part of the algorithm and test it out before moving on to the next step.

Extend the ```animals.csv``` file to include animals of your choice, then re-run your code.

### Activity 4 - Building bank accounts

Type in the code from Version 3 of the Bank Accounts example in the lecture 
slides. The class definitions should be in ```accounts.py``` and the driver code in 
```testAccounts.py```. Test (run) the code to see that it works as shown in the lecture.

### Activity 5 - Simulating bank account transactions

We are going write some new code ```banking.py``` to allow the user to choose a transaction, 
account and optional amount to run transactions on one account. This will be in a 
loop that also allows for printing all the current balance. We are working towards 
something similar to the bucketlist builder...

1. Import classes
2. Create variables
  2. build bank account object ```(‘Everyday’,‘007’,3000)```
3. Request transaction selection: ```withdrawal, deposit, interest, balance or exit```. e.g. W for Withdrawal, D for deposit, I for interest, B for balance and X for eXit
4. While exit is not selected
  4. If ‘W’ – ask for amount then call withdraw method
  5. Else if ‘D’ – ask for amount then call deposit method
  6. Else if ‘I’ – call interest method
  7. Else if ‘B’ – print balance
  8. Request transaction selection

### Activity 6 - Improving bank account code

The code for requesting the transaction selection is quite cumbersome. Copy ```banking.py``` 
to ```banking2.py``` and add a new function: ```chooseTrans()``` which will:

1. Prompt for the transaction selection
2. Check that it is valid (while not valid, ask again) 
3. Return the choice

Update ```banking2.py``` to use the function in **both** places it is required.

### Submission

Update the README file to include all files created in this practical.

All of your work for this week’s practical should be submitted via Blackboard using
the Practical 06 link. This should be done as a single "zipped" file.
Submit the resulting file through Blackboard. (refer to Practical 00 or 01 for instructions
on zipping files.
 
There are no direct marks for these submissions, but they may be taken into account 
when finalising your mark for the unit. Go to the Assessment link on Blackboard and 
click on Practical 03 for the submission page.

### And that's the end of Practical 06!

::::::::::::::::::::::::::::::::::::: keypoints 

- We can model real world items as objects
- The template for an object is its **class** - which we can use to make lots of objects
- Objects know their state (data) and behaviour (methods) and are responsible for choosing who can access their data, and how... we can trust them to maintain a **valid** state
- The convention is to use a capital letter for the class name, and lowercase for variables (which can hold objects)
- If we create a dog object ```d1 = Dog("Brutus")```, we call its methods as ```d1.sit()``` and can access data as ```d1.name``` or through a method e.g. ```d1.getName()```. Accessing the data directly is often easier, but can be risky...
  1. Could alter data and make it invalid
  2. Requires knowledge of the internal workings of the object - which is against OO principles 

:::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: checklist

### Reflection
 
1. **Knowledge:** What is the difference between a class and an object?
3. **Comprehension**: What is the difference in the code used to define a class,
and the code used to define an object?
5. **Application**: How would you write a new class to represent a rabbit?
7. **Analysis**: What is the difference between ```garfield.printit()``` and ```print(garfield)```?
Which would you use and why?
9. **Synthesis**: How would you modify the pet classes in ```animals.py``` to include a
microchip number for cats and dogs?
10. **Evaluation**: Task 5 takes in user input to determine the transactions and
amounts if required. What parts of this should have validation to make the code 
more robust? (less likely to crash if given the wrong input)

::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: challenge

For those who want to explore a bit more of the topics covered in this practical. Note that the challenges are not assessed but may form part of the prac tests or exam.

1. Add class variables and methods to ```Dog, Cat and Bird``` to represent how they move (```self.moves```), and to ```getMoves()```. These will be **class** variables as they will apply to all objects of that class.
3. Extend ```banking.py``` to have three bankaccounts in a list. Modify your code to ask for the account for each transaction
 
::::::::::::::::::::::::::::::::::::::::::::::::
