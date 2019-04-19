
n = int(input())
ans = 0
for i in range(1,n+1):
    
    ans = ans + i # 1 ~ n
    if i == 100:
        break
print(ans)
