#!/usr/bin/python
# Filename:str_methods.py

name='Swaroop'

if name.startswith('Swa'):
    print('yes.the string starts with"Swa"')

if 'a' in name:
    print('yes,it contacts the string "a"')

if name.find('war')==1:
    print('yes,it contains the string "war"')

delimiter='弱于'
mylist=['Brazil','Russia','India','China']
print(delimiter.join(mylist))
