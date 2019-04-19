n = int(input())

for i in range(1,n+1):
    #如果 這次要印的樓層是4樓的話
        #就跳過
    if i==4:
        continue
    print('floor',i)
