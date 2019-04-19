n = int(input())
ans = 0
for i in range (1,n+1):
    ans = ans +i
    print(i,end='')
    if i!=n:#如果這次的迴圈不是最後一次的話就印出+
        print('+',end='')
else:
    print(' =',ans)

'''
n=eval(input())
 
total=0
for i in range(1,n+1):
    total += i
    print(i,end='')
    if (i<n):
        print('+',end='')
print (' =',total)
'''
