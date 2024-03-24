"""
errorful.py - a program full of errors to demonstrate how Python responds

Usage guide: 
    comment out or correct each section so the next section of code will run and crash

"""

# runtime error - integer conversion
mynum = int("42")
print(mynum)

# runtime error - index out of range
mylist = [1, 2, 3, 4]
print(mylist[len(mylist)-1])

# syntax error - string not ended
print("Hello, hello, hello!")

# runtime error - missing file
with open('workfile.csv', 'r') as f:
    line = f.readline()
    contents = []
    while line:      # while not end of file
        linelist = line.split(',')
        contents.append(linelist)
        line = f.readline()

# exception handling for more robust fileIO

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    print(i)
except OSError as err:         # on open or read - missing or corrupt
    print("OS error detected:", err)
except ValueError:             # on int() conversion
    print("Could not convert data to an integer.")

