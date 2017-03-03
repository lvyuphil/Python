#!/usr/bin/python
# Filename: 11.3 class_init.py

class Person:
    def __init__(self,name):
        self.name = name
    def sayHi(self):
        print('Hello,my name is',self.name)

p=Person('Swaroop')
p.sayHi()

Person('Swaroop').sayHi()
