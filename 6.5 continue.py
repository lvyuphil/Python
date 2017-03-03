#!/usr/bin/python
#Filename: continue.py


while True:

    s = input('Enter something:')
    if s=='quit':
        break
    if len(s)<3:
        continue
    print ('Length of the string is',len(s))
    print('Input is of sufficient length')
