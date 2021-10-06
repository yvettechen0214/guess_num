import random

start = int(input("請決定隨機數字範圍開始值："))
end = int(input("請決定隨機數字範圍結束值："))

r = random.randint(start,end)
count = 0
while True:
    count += 1   #count = count + 1
    user_guess = int(input("請輸入您猜的數字："))
    if user_guess == r:
        print("你猜對了")
        print("這是你猜的第", count, "次")
        break
    else:
        if user_guess > r:
            print("比答案大")
        else:
            print("比答案小")
    print("這是你猜的第", count, "次")