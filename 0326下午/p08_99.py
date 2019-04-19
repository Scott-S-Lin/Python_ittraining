n = int(input())

h = w = n

for i in range(1,h+1):
    for j in range(1,w+1):
        print(i,'*',j,'=',i*j,sep='',end='\t')
    print()

