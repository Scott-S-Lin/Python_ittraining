
# 7:{1,7}
#10:{1,2,5,10}
# 9:{1,3,9}

n = int(input())

fct = 0
for i in range(1,n+1):
    if n%i==0:
        fct += 1
else:
    if fct == 2:
        print(n, 'is prime')
    else:
        print(n,'is not prime')


