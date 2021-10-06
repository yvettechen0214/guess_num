import random

r = random.randint(1,100)

while True:
    user_guess = int(input("請輸入您猜的數字："))
    if user_guess == r:
        print("你猜對了")
        break
    else:
        if user_guess > r:
            print("比答案大")
        else:
            print("比答案小")