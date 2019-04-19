h = int(input())
w = int(input())

for i in range(1,h+1):
  for j in range(1,w+1):
    print("%d*%d=%2d "%(i,j,i*j),end='')
print()
