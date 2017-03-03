#!/usr/bin/python
# Filename: objvar.py 使用类与对象的变量

class Person:
    '''Represents a person''' #docstrings
    population = 0  # population是类的变量

    def __init__(self,name): # name是对象的变量 
        '''Initializes the person's data'''# 初始化person资料
        self.name = name
        print('（Initialing %s）'%self.name)

        # 当这个人的资料被创建，TA将加入到population中去
        Person.population += 1 # 'a+=1'等价于‘a=a+1’

    def __del__(self):
        '''I am dying.'''
        print('%s says bye'%self.name)
        Person.population -= 1

        if Person.population == 0:
            print('i am the last one.')
        else:
            print('There are still %d people left.'%Person.population)

    def sayHi(self):
        '''Greeting by the person.

Really,that's all it does.'''
        print('Hi,my name is %s.'%self.name)

    def howMany(self):
        '''Prints the current population.'''
        if Person.population == 1:
            print('i am the only person here.')
        else:
            print('We have %d persons here.'%Person.population)

swaroop = Person('Swaroop')
swaroop.sayHi()
swaroop.howMany()

kalam = Person('Abdul Kalam')
kalam.sayHi()
kalam.howMany()

swaroop.sayHi()
swaroop.howMany()

del(swaroop)
del(kalam)
