#!/usr/bin/python
# Filename:10.2 backup_ver2.py


import os
import time

source=[r'G:\python\test',r'D:\report_data2.txt']#带备份文件和目录列表

target_dir = r'G:\python\backup'

today = target_dir+os.sep+time.strftime('%Y%m%d')

now = time.strftime('%H%M%S')

if not os.path.exists(today):# 用os.exists函数检验在主备份目录中是否有以当前日期作为名称的目录
    os.mkdir(today) # 如果没有，使用os.mkdir函数创建
    print('Successful created directory',today)
    

target = today + os.sep + now + '.zip'

# target = target_dir + os.sep+time.strftime('%Y%m%d%H%M%S') + '.zip'


# 待创建归档的名称
# os.sep 为linux中的‘/’和windows中的‘\’。os.sep根据系统自动检测
# print(target)

rar_command='WinRAR a %s %s'%(target,' '.join(source))
# a是RAR的参数 #.join(X)是在X的每个字符串之间用“_”连接



print(rar_command)

if os.system(rar_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
 
