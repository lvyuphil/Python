#!/usr/bin/python
# Filename: 13.2 raising.py 引发异常

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self,length,atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    s = input('Enter something-->')
    if len(s)<3:
        raise ShortInputException(len(s),3) # 引发异常
    # Other work can continue as usual here


except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as x:
    print('ShortInputException:The input was of length %d,\
was expecting at least %d'%(x.length,x.atleast))

    if isinstance(x,ShortInputException):
        print("x is an instance of ShortInputException")

else:
    print('No exception was raised')
