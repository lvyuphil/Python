#!/usr/bin/python
# Filename: 11.2 method.py

class Person: 
    def sayHi(self): #和一般函数 def sayHi() 只是多一个额外的self变量
        print('Hello,how are you?')

p = Person()
p.sayHi()
#两者等价   
Person().sayHi()
