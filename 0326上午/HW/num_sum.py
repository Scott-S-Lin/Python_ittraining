n = int(input('請輸入一數字：'))
ans = 0
for i in range (1,n+1):
    ans = ans +i
    print(i,end='')
    if i!=n:
        print('+',end='')
    else:
        print(' =',ans)
