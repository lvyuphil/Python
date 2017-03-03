# !/usr/bin/python
# Filename while.py

number=23
running=True

while running==True:
    guess=int(input('enter an integer:'))
    if guess==number:
        print('牛逼你猜对了')
        running=False
        print('The loop is over.')
    elif guess<number:
        print('低了')
    else:
        print('高了')

print('Done')
