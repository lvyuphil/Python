#!/usr/bin/python
# Filename:cat.py

import sys
import time

def readfile(filename): #从文件中读出文件内容
    ''' Print a file to the standard output.'''

    f = open(filename)# file？
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line),# 分别输出每行
    f.close()

# 脚本从这里开始  Script starts from here

if len(sys.argv)<2:  # 即只存在sys.argv[0]即只存在地址,没有参数输入
    print('No action specified')
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    #这是一个二维数组，把argv[1]这个参数的下标为[2],即第三个字符开始直到结束的字符串复制给option
    #如果是--help,则这之后option为help

    if option == 'version':
        print('Version 1.2')
    elif option == 'help':
        print('''\
This program prints files to the standard output.
Any number of files can be specified明确规定的)
Options include:
-- version:Prints the version number
-- help   :Display this help''')
    else:
        print('Unknown option.')
        sys.exit()

              
else:  #如果命令行参数不是以'--'格式开始的，那么就是文件了,所以执行西段代码
    for filename in sys.argv[1:]: #当参数为文件名时，传入readfile，读出其内容
        readfile(filename) # 执行readfile函数

              
