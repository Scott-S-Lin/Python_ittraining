MaxVal = 0 #目前已知最大的數字
MaxPos = 0 #目前已知最大的數字的位置

n = eval(input())
sum1 = 0
ct = 0
while n != -1:
    #print(n)
    sum1 += n
    ct = ct+1

    #如果 這次的輸入(n) 比 目前已知最大的數字 還大的話
        #就把 這次的輸入(n) 當成 目前已知最大的數字(MaxVal)
        #還要記錄 這次的輸入的次數(ct) 成為 目前已知最大的數字的位置(MaxPos)
    if n > MaxVal:
       MaxVal = n
       MaxPos = ct

    n = eval(input())    
else:
    print(sum1)
    print(sum1/ct)
    print(MaxVal)
    print(MaxPos)
