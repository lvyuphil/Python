#!/usr/bin/python
# Filename:reference.py

print('Simple Assignment')
shoplist=['apple','mango','carrot','banana']
mylist=shoplist #my list is just another name pointing to the  same object!

del shoplist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)

print('Copy by making a full slice')
mylist=shoplist[:]#切片操作符创建拷贝
del mylist[0]

print('shoplist is',shoplist)
print('mylist is',mylist)

del shoplist[0]

print('shoplist is',shoplist)#创建拷贝后即使继续对原列表进行修改，
#也不印象拷贝列表
print('mylist is',mylist)
