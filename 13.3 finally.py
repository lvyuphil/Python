#!/usr/bin/python
# Filename: 13.3 finally.py

import time


poem = '''\
Programming is fun
When the word is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt','w') # ‘w’is writing ,在python3中，open() replaced file()
f.write(poem) # write text to file
f.close() # close the file

try:
    f = open('poem.txt')
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print(line),
finally:  # 程序运行过程中无论发生什么情况都执行关闭文件
    f.close()
    print('Cleaning up...closed the file')
    print('6666')
