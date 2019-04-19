st = []
n = int(input())
while n != -1:
    st.append(n)
    n = int(input())
#print(st.sort())  印出None 列印回傳值
#因為改變的內容已經寫進去list
#回傳需要浪費記憶體資源
'''
有沒有回傳值
迴傳值是什麼型態
關係到你可不可以印出來
可不可以加中括號、可不可以打點使用某些方法
'''
st.sort()
print(st)
