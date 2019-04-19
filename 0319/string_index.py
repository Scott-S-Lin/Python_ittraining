s = input()
f = input()
index = -1
while 1:
    index = s.find(f,index+1)
    if(index == -1):
        break
    print(index)
