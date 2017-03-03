#!/usr/bin/python
# Filename: 12.2 pickling.py


import pickle as p # python 3.x中 cPickle变成了pickle

shoplistfile = 'shoplist.data' 

shoplist = ['apple','mango','carrot']

f = open(shoplistfile,'wb')
p.dump(shoplist,f) # dump the object to a file 储存dump
f.close()

del shoplist # remove the shoplist

# Read back from the storage

f = open(shoplistfile,'rb') # 默认为‘rb’ead

storedlist = p.load(f) # 取储存 load

print(storedlist)

# 把 shoplist 储存到 shoplistfile中，即使delete掉shoplist
# 仍能在 shoplistfile中取出（load）相对应的内容
