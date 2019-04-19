n = int(input())

h = w = n
# h 共要印幾(h)列的*號 (高度)
for i in range(h):
    # i 現在要印的是第幾(i)列
    #print(i,end=" ")
    # w 這一列印幾(w)個*號(寬度)

    # n = 5
    # i = 0,1,2,3,4
    #n-i= 5,4,3,2,1
    w = n-i
    
    for j in range(w):
        # j 現在印這一列的第幾(j)個*號
        print('*',end='')
    print()

