n = int(input())
num = 1
for i in range(n):
    for j in range(i+1):
        print(num,end=' ')
        num += 1
    print()

'''
#正向三角形
h = int(input())

for i in range(h):  
    print(i,end=" ")
    w = i+1
    for j in range(w):
        print('*',end='')
    print()


'''

