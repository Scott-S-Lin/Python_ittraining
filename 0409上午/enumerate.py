ary = [11,22,33,44,55]
'''
for e in ary:
    print(e)
print()
for i in range(len(ary)):
    print('#',i,sep='')
'''
for i,e in enumerate(ary,0):
    print(i,e)
