#!/usr/bin/python
# Filename: 12.1 using_file.py



poem = '''\
Programming is fun
When the word is done
if you wanna make your work also fun:
    use Python!
'''

f = open('poem.txt','w') # ‘w’is writing ,在python3中，open() replaced file()
f.write(poem) # write text to file
f.close() # close the file

f = open('poem.txt') # there is no 'r'or 'w'
# if no mode is specified,'r'(read) mode is assumed by default 默认

while True:
    line = f.readline()
    if len(line) == 0: # zero length indicates EOF(enf of file)
        break
    print(line),
    # ','避免自动换行
# 在一个循环中，我们使用readline方法读文件的每一行。这个方法返回包括行末换行符的一个完整行。
# 所以，当一个 空的 字符串被返回的时候，即表示文件末已经到达了，于是我们停止循环。

f.close()
