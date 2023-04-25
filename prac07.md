---
title: "Prac07: Object Relationships and Exception Handling"
---

:::::::::::::::::::::::::::::::::::::: questions 

- How can we work with collections of objects?
- How can we make use of common state and behaviour to organise objects using a hierarchy of classes?
- Where can we use exceptions to make our code more robust?

::::::::::::::::::::::::::::::::::::::::::::::::

::::::::::::::::::::::::::::::::::::: objectives

1. Understand and apply class relationships: composition, aggregation and inheritance
2. Understand and use exception handling

::::::::::::::::::::::::::::::::::::::::::::::::

### Introduction

In this practical we will see how to create relationships between objects. Exceptions are an important concept in OO programming. We will add exceptions to our code.

### Activity 1 - Setting up an animal shelter

The lecture notes outline an implementation of an animal shelter class. This class includes 
lists of animals – which is an aggregation relationship. The shelter "has" animals.

Type in the code below as ```shelters.py``` and copy and modify ```animals.py``` from Practical 6 as shown
in the next code snippet. These match the code given in the Lecture 7 slides.

**shelters.py**
```python
from animals import Dog, Cat, Bird, Shelter 

print('\n#### Pet shelter program ####\n')

rspca = Shelter('RSPCA', 'Serpentine Meander', '9266000') 

rspca.newAnimal('Dog', 'Dude', '1/1/2011', 'Brown', 'Jack Russell') 
rspca.newAnimal('Dog', 'Brutus', '1/1/1982', 'Brown', 'Rhodesian Ridgeback')
rspca.newAnimal('Cat', 'Oogie', '1/1/2006', 'Grey', 'Fluffy') 
rspca.newAnimal('Bird', 'Big Bird', '10/11/1969', 'Yellow', 'Canary') 
rspca.newAnimal('Bird', 'Dead Parrot', '1/1/2011', 'Dead', 'Parrot')

print('\nAnimals added\n')

print('Listing animals for processing...\n') 

rspca.displayProcessing()

# This code is commented out until you have implemented 
# the methods in animal.py
#print('Processing animals...\n')
#rspca.makeAvailable('Dude') 
#rspca.makeAvailable('Oogie') 
#rspca.makeAvailable('Big Bird') 
#rspca.makeAdopted('Oogie')
#print('\nPrinting updated list...\n') 
#rspca.displayAll()
```
**animals.py**
```python
# Cat, Dog, Bird definitions from Prac 7 should be here 
class Shelter():
    def __init__(self, name, address, phone): 
        self.name = name
        self.address = address
        self.phone = phone
        self.processing = [] 
        self.available = [] 
        self.adopted = []
        
    def displayProcessing(self): 
        print('Current processing list:') 
        for a in self.processing:
            a.printit() 
        print()
    
    def displayAvailable(self): 
        ... # add your code here
    
    def displayAdopted(self): 
        ... # add your code here
    
    def displayAll(self): 
        self.displayProcessing()
        #self.displayAvailable()
        #self.displayAdopted()
    
    def newAnimal(self, type, name, dob, colour, breed): 
        temp = None
        if type == 'Dog':
            temp = Dog(name, dob, colour, breed) 
        elif type == 'Cat':
            temp = Cat(name, dob, colour, breed) 
        elif type == 'Bird':
            temp = Bird(name, dob, colour, breed) 
        else:
            print('Error, unknown animal type: ', type) 
        if temp:
            self.processing.append(temp) 
            print('Added ', name, ' to processing list') 
        
    def makeAvailable(self, name): 
        ... # add your code here

    def makeAdopted(self, name): 
        ... # add your code here
```

### Activity 2 - It's a family affair

In the lecture we created a parent (super) class ```Animal``` to factor out the 
repetition in ```Cat, Dog and Bird```. This is an inheritance relationship – ```Cat``` "is an" ```Animal```.
Edit ```animals.py``` and add in the modified class definitions for ```Dog``` and ```Bird```. 
Re-run ```shelters.py``` after making the changes to see that everything still works.

```python
class Animal():
    myclass = "Animal"

    def __init__(self, name, dob, colour, breed): 
        self.name = name
        self.dob = dob
        self.colour = colour
        self.breed = breed

    def __str__(self):
        return(self.name + '|' + self.dob + '|' + self.colour + '|' + self.breed)

    def printit(self):
        spacing = 5 - len(self.myclass) 
        print(self.myclass.upper(), spacing*' ' + ': ', self.name,'\tDOB: ', 
                self.dob,'\tColour: ', self.colour,'\tBreed: ', self.breed)

class Dog(Animal): 
    myclass = "Dog"
    
class Cat(Animal): 
    myclass = "Cat"

class Bird(Animal): 
    myclass = "Bird"
```

### Activity 3 - People are People

In the lecture we saw the above class diagram for people, students and staff. 
We will now implement that structure and then read information from files using 
regular expressions to split out the data.

**people.py**
```python
class Address():
    def __init__(self, number, street, suburb, postcode): 
        self.number = number
        self.street = street
        self.suburb = suburb
        self.postcode = postcode
        
    def __str__(self):
        return(self.number + ' ' + self.street + ', ' + self.suburb + ', ' + self.postcode)

class Person():
    def __init__(self, name, dob, address): 
        self.name = name
        self.dob = dob
        self.address = address
        
    def displayPerson(self):
        print('Name: ', self.name, '\tDOB: ', self.dob) 
        print(' Address: ', str(self.address))
```
**testPeople.py**
```python
from people import Address, Person 
print('#### People Test Program ###')
testAdd = Address('10', 'Downing St', 'Carlisle', '6101') 
testPerson = Person('Winston Churchill', '30/11/1874', testAdd) 
testPerson.displayPerson()
```

Run ```testPeople.py``` to see its output. Add in another test person and re-run the program.

Now we can add in a sub-class for Staff. We don't want to duplicate code, so, where possible, 
we will use ```super()``` to call the methods from the parent class. Modify ```people.py```
and ```testPeople.py``` to include the code below.

**testPeople.py**
```python
from people import Address, Person, Staff 

print('#### People Test Program ###')
testAdd = Address('10', 'Downing St', 'Carlisle', '6101') 
testPerson = Person('Winston Churchill', '30/11/1874', testAdd) 
testPerson.displayPerson()
print()
testAdd2 = Address('1', 'Infinite Loop', 'Hillarys', '6025')
testPerson2 = Staff('Professor Awesome', '1/6/61', testAdd2, '12345J') 
testPerson2.displayPerson()
print()
```
**people.py**
```python
# existing code here 
class Staff(Person):
    myclass = 'Staff'
    def __init__(self, name, dob, address, id): 
        super().__init__(name, dob, address) 
        self.id = id
        
    def displayPerson(self): 
        super().displayPerson() 
        print(' StaffID: ', self.id)
```

### Activity 4 - Shower the People

So, we have People and Staff classes. We can follow the same pattern to create students, 
postgrad students and undergrad students: (update ```people.py```)

- Student class
  - extend Person
  - add a Student ID instance variable
  -  update the myclass class variable to be 'Student'
- Postgrad class
  - extend Student
- Undergrad class
  - extend Student
  -  update the myclass class variable to be 'Undergrad' 

Update ```testPeople.py``` to include values to test the new classes.


### Activity 5 - Universal People Reader

Now we can connect up some concepts from across the semester to load up 
a list of people. We will read in people data from a file, split it by a 
delimiter (':'), extract fields create objects and add them into the list.

What we will need in our code is:

1. Import classes
2. Create variables (e.g. empty list for the people) 
3. Open file
4. For each line in the file
  - Split line into class, name, dob, address
  - Create person object to match first field in the entry 
  - Add the new person to the list
5. Print person list

Here is the sample file – you can copy and paste it into vim: ```people.csv```

**people.csv**
```
Staff:Professor Michael Palin:1/6/61:1 Infinity Loop, Balga, 6061:5555J 
Postgrad:John Cleese:1/9/91:16 Serpentine Meander, Gosnells, 6110:155555 
Undergrad:Graham Chapman:7/9/97:80 Anaconda Drive, Gosnells, 6110:166666 
Undergrad:Connie Booth:8/9/98:10a Cobra St, Dubbo, 2830:177777
```

We can split the input on ':' to separate the class, name, dob, address and ID.


### Activity 6 - Exceptional People Reader

As a final part to this practical, we can add exception handling to our program. 
One of the riskiest areas of code is working with files. We can update the code 
from Task 5 to add exception handling around the file open/read/close. We should 
always have exception handling around file input and output.

```
try:
    with open('people.csv', 'r') as f: 
        lines = f.readlines()
except OSError as err:
    print('Error with file open: ', err)
except:
    print('Unexpected error: ', err)
```

Change the code to request the file name from the user, then test what happens 
if the file does/does not exist. Put this code into a loop to keep requesting the 
filename until it is entered correctly.

### Activity 7: - Extra-exceptional People Reader 

Change the code from Activity 6 to raise an invalid value error when the date of birth 
is invalid (there are many ways for it to be invalid - choose one). This should be be 
chacked in the init function of the Person class. You will then need to put try/catch 
around the creation of the objects. Print a message to show the user which record(s) are incorrect.

Create a new input file to test this functionality.

Imagine if this was a very large input file... just printing to the screen for each error could give 
a large and confusing output. Update your code to ***write to*** a file ```errorLog.txt``` each time 
an error occurs from reading in the data and creating objects.

### Submission

Create a README file for Practical 7. Include the names and descriptions 
of all of your files from today.

All of your work for this week’s practical should be submitted via Blackboard 
using the link in the Week 7 unit materials. This should be done as a single "zipped" file.

### And that's the end of Practical 07!

::::::::::::::::::::::::::::::::::::: keypoints 

- Classes are templates for creating objects
- We can define classes to have objects *contain* other objects or *inherit from* a class heirarchy
- We should define methods to allow communication with objects, and may have multiple levels of methods to work with collections and/or inheritance
- Exception handling helps us make our code more robust by adding exception handling where errors might occur.

:::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: checklist

### Reflection
 
1. **Knowledge:** Define class variables and instance variables - how are they different? (note that we use specific meanings for them in this unit, they are often considered synonyms)
3. **Comprehension**: If a class variable is changed, e.g. ```BankAccount.interest_rate
= 0.02``` in ```accounts.py```, which objects are affected? 
5. **Application**: How would you setup multiple shelters in ```shelters.py```?
7. **Analysis**: In Task 2 the method ```__str__``` was added to the ```Animal``` class. What does it do and how does it improve the classes?  
9. **Synthesis**: Describe what could you do to make your code more robust? (Hint: testing and exceptions)  
10. **Evaluation**: Two approaches to checking for errors when converting a string to an integer are: to check formatting before trying a risky function; or to check for exceptions. Why would the latter be preferred?
::::::::::::::::::::::::::::::::::::::::::::::::

:::::::::::::::::::::::::::::::::::::::::::::::: challenge

For those who want to explore a bit more of the topics covered in this practical. Note that the challenges are not assessed but may form part of the prac tests or exam.

1. Extending Activity 5, add phone numbers to the input file ```people.csv```, then add in code to read in the phone numbers.  
2. Add exception handling to the accounts programs from last week. Each numeric input should be protected and checked with try/except clauses.  
3. Extending Activity 2, add in a class to represent rabbits and then write code to test it.  
4. Extending Activity 2, add an instance variable for holding the microchip information for cats and dogs in the animal shelter example. Birds do not have microchips, so it shouldn’t be in (or inherited into) their class definition.
 
::::::::::::::::::::::::::::::::::::::::::::::::
