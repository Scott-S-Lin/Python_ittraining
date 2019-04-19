import random

#程式變數初始化
#ct = 0
Max = 100
Min = 1
ans = random.randint(1,100)
print(ans)
#重複判斷 使用者輸入正不正確

while True:
    print('請輸入',Min,'< ? <',Max,'範圍的數字：',end='')
    guess = int(input())
    #if Min < guess < Max: #如果在範圍內的話
    #等於 if guess > Min and guess < Max:
    
    if guess < Min or guess > Max:
        print('out of range')
    else:
        
        if guess == ans:
            print('Bingo, you are right!')
            break
        elif guess > ans:
            Max = guess
            print('猜太大')
        elif guess < ans:
            Min = guess
            print('猜太小')



