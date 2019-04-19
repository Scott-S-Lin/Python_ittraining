#01
keys = ('P','M','H')
values = 'Pikachu','Mickey Mouse','Hello kitty'

d1 = dict(zip(keys,values))
# d1 = {'P':'Pickachu','M':'Mickey Mouse','H':'Hello kitty'}

#02
qkey = input()
while qkey != '-1':
    if qkey == '-2':
        print(d1)
    else:
        print(d1[qkey])
    qkey = input()
