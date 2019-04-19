
n = int(input())

ans = 1
print(1,end='')
for i in range(2,n+1):
    ans = ans + i # 2 ~ n
    print('+',end='') #就印出 + 號
    print(i,end='')
else:
    print(' =',ans)
