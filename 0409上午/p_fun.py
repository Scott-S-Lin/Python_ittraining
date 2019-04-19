def f1(n,m):
    print('f1() n*m =',n*m)
    
def f2(n,m):
    n-=1
    return n


n = int(input())
m = int(input())
f1(n,m)
print(f2(n,m))
