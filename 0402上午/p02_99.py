h = int(input())
w = int(input())

for i in range(0,h):
    for j in range(1,w+1):
        print("%d*%d=%d"%(i+1,j,i*j),end='')
    print()
