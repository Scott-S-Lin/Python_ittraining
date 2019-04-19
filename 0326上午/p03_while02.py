
n = eval(input())
sum1 = 0
ct = 0
while n != -1:
    #print(n)
    sum1 += n
    ct = ct+1

    n = eval(input())    
else:
    print(sum1)
    print(sum1/ct)
