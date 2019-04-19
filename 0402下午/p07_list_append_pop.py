
n = int(input())
st1 = []#先宣告一個空的list
#從n到1 要包含1
for i in range(n,0,-1):
    print('data',i)
    st1.append(i)#i放進去st1

print()
#從後面取資料->pop st1.pop()
#迴圈拿資料 順便印出data
for i in range(n):
    print('data',st1.pop())
