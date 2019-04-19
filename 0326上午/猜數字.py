import random
n = int(input('請輸入數字範圍n='))
bomb = random.randint(1,n)

while True:
    s = int(input('請輸入1~%d的數字:'%n))
    if s == bomb:
        print('Yes')
        break
    else:
        print('No')
        
