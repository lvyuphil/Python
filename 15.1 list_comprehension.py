#!G:\\python\\code
# Filename: 15.1 list_comprehension.py

listone = [2,3,4]
listtwo = [2*i for i in listone if i>2]
print(listtwo)


def powersum(power,*args):

    total = 0
    for i in args:
        total += pow(i,power) #math.pow（i.power） 返回 i^power
        print('\npow in this step',pow(i,power))
        print('\nthis step\'s total is',total)

    return total


# 所有多余的函数参数都会作为一个元组存储在args中
# 例如 输入参数powersum（2，3，4，5，6），即 power = 2 ，*args=(3,4,5,6)
    
