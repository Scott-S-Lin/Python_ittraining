
n = int(input())
ans = 0
for i in range(1,n+1):
    ans = ans + i # 1 ~ n
    print(i,end='')
    #如果 這次的迴圈不是最後一次的話(i, n)
print('after loop',i)
if i!=n:
    print('+',end='') #就印出 + 號
else:
    print(' =',ans)
