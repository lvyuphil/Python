#!/usr/bin/python
#Filename:func_docstrings.py

def printMax(x,y):
    '''Prints the maximum of two number.

the two values must be integers.'''
    x=int(x) #convert to integers,if possible
    y=int(y)

    if x>y:
        print(x,'is maximum')
    else:
        print(y,'is maximum')
printMax(3,5)

print(printMax.__doc__)
help(printMax)
