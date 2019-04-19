keys = ('P','M','H')
values = 'Pikachu','Mickey Mouse','Hello kitty'
d1 = dict(zip(keys,values))
# d1 = {'P':'Pickachu','M':'Mickey Mouse','H':'Hello kitty'}

#要一直重複執行但不知道要執行幾次的迴圈

while True:
    qkey = input()
    #print(d1[qkey])
    # 如果輸入是 -1 的話就
        # 離開迴圈
    if qkey == '-1':
        break
    
    # 如果 輸入的key 存在字典裡的話，
        #就印出對應的value
    elif qkey in d1:
        print(d1[qkey])
    
    # 不然的話 就
        #提示使用者 此 key 不存在
        #令使用者可輸入對應文key值的value
        #新增的對應文字組成一筆key&value
    else:
        print(qkey,'not exist.')
        n = input('Please enter a value:')
        d1[qkey] = n

