#!/usr/bin/python
# Filename:10.1 backup_ver1.py


import os
import time

source=[r'G:\python\test',r'D:\report_data2.txt']#带备份文件和目录列表

target_dir = r'G:\python\backup'

target = target_dir + os.sep+time.strftime('%Y%m%d%H%M%S') + '.zip' #待创建归档的名称
#os.sep 为linux中的‘/’和windows中的‘\’。os.sep根据系统自动检测
print(target)

rar_command='WinRAR a %s %s'%(target,' '.join(source))
#a 是RAR的参数 #.join(X)是在X的每个字符串之间用“_”连接



print(rar_command)

if os.system(rar_command)==0:
    print('Successful backup to',target)
else:
    print('Backup FAILED')
 
