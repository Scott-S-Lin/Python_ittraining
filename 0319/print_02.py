# 一般輸出
print('testing')

# 加上保留字
print('print with reserved words including「\'」「\"」「\\」「\b」')  


# 利用\t 實現對齊輸出
print('姓名\t年齡')

# 即使字數不同也可以對齊
print('王小明\t16 歲')	

# 若超出一個Tab 鍵距離就無法對齊？
print('吉多·范羅蘇姆\t63歲', end = '\n\n')  


# 可以利用兩組\t 來實現較長的對齊
print('姓名\t\t年齡')
print('王小明\t\t16 歲')
print('吉多·范羅蘇姆\t63 歲')  

