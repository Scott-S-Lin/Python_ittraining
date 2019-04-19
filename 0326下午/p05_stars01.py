#正方形
n = int(input())

h = w = n# h 共要印幾(h)列的*號 (高度)

for i in range(h):
    print(i,end=" ")# i 現在要印的是第幾(i)列
    for j in range(w):# w 這一列印幾(w)個*號(寬度)  
        print(j,'',end='')# j 現在印這一列的第幾(j)個*號
    print()

