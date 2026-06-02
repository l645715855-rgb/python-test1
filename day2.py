"""1-100猜数字游戏"""
import random

secret = random.randint(1,100)
print("欢迎来到猜数字游戏")

quantity = 1
test = int(input("请输入数字"))
while test != secret:
    quantity = quantity + 1
    if test < secret:
        test = int(input("你猜小了，请输入数字"))
    elif test > secret:
        test = int(input("你猜大了，请重新输入"))
    
if test == secret:
    print(f'恭喜你猜对了，数字是{secret},你用了{quantity}次')
