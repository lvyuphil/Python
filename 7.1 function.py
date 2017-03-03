def sayHello():
    print ('Hello World!') # block belonging to the function

number=4

while True:
    guess=input('input something:')
    length=len(guess)
    
    if guess=='quit':
        break
    if length==number:
        sayHello() # 调用函数
        break
