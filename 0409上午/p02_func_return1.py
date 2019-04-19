
def f1(n,m):
    print('f1() n*m =',n*m)
    
def f2(n,m):
    return n*m

n1 = 5
n2 = 10
f1(n1,n2)

ans = f2(n1,n2)
print('f2() n*m =',ans)
print('相乘的結果 =',ans)
print('f2() + 50 =',ans+50)
