keys = ('P','M','H')
values = 'Pikachu','Mickey Mouse','Hello kitty'
d1 = dict(zip(keys,values))


while True:
    qkey = input()
    
    # 如果輸入是 -1 的話就
        # 離開迴圈  
    # 如果 輸入的key 存在字典裡的話，
        #就印出對應的value
    # 不然的話 就
        #提示使用者 此 key 不存在
        #令使用者可自行新增對應文字組成一筆key&value
    
    if qkey == '-1':
        break
    if qkey in d1:
        print(d1[qkey]) 
    else:
        print(qkey,'does not exist. Enter a new one:')
        d1[qkey]=input()
