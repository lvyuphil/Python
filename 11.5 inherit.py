#!/usr/bin/python
# Filename:11.5 inherit.py

class SchoolMember:
    '''represents any school member'''
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print('(Initialazed SchoolMember:%s)'%self.name)

    def tell(self):
        '''Tell my details.'''
        print('Name:"%s" Age:"%s"'%(self.name,self.age))

class Teacher(SchoolMember):
    '''represents a teacher.'''
    def __init__(self,name,age,salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print('(Initialazed Teacher:%s)'%self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:"%d"'%self.salary)

class Student(SchoolMember):
    '''represent a student.'''
    def __init__(self,name,age,marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print('(Initialazed Student:%s)'%self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:"%d"'%self.marks)

t = Teacher('Mr.Li',40,30000)
s = Student('Swaroop',23,85)

print

members = [t,s]

for member in members:
    member.tell()
