#!G:\\python\\code
# Filename: 15.2 lambda.py


#def make_repeater(n):
#    return lambda s:s*n # 在运行时创建新的函数对象s*n，s为心

## s为lambda的参数；
## s*n为lambda的表达式
## 表达式的值被这个新建的函数返回

#twice = make_repeater(10)

#print(twice('word'))

#print(twice(5))

## exec 执行字符串或文件中的python语句

#exec('print("hello world")')

## eval执行储存在字符串中的有效python表达式

#eval('2*3')

## assert 语句用来声明某个条件是真的

mylist = ['item','abc','123','666']

assert len(mylist) >= 1

mylist.pop(2) # 默认参数为提出列表中最后一个
# .pop(obj=list[-1])
# obj:可选参数，对象的索引，从名单中提出
# 0为第一个，1为第2个，2为第三个，不填为第-1个即最后一个
# 返回：返回从列表中删除的对象 
