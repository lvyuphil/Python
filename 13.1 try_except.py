#!/usr/bin/python
# Filename: 13.1 try_except.py

import sys

try:
    s = input('Enter something-->')


except EOFError:
    print('\nWhy did you do an EOF on me?')
    sys.exit() # exit the program
    
except:
    print('\nSome error/exception occurred') # here ,we are not exiting program

print('Done@')
