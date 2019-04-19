x=eval(input())
for m in range(2,x):
    fct=0 #計數器，紀錄該數值有幾個因數
    for i in range(2,m):
        if(m%i==0):
            fct+=1
    if(fct==0):
        print(m,'is prime')
