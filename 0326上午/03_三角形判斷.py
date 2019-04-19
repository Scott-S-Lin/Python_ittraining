'''
a=int(input())
b=int(input())
c=int(input())
 
if a+b<=c or b+c<=a or c+a<=b:
    print('False')
    import sys;sys.exit()
else:
    print('True')
 
if a>b and a>c:
    if a**2==b**2+c**2:
        print('Right Triangle')
    else:
        print('Non-Right Triangle')
elif b>c:
    if b**2==a**2+c**2:
        print('Right Triangle')
    else:
        print('Non-Right Triangle')
else:
    if c**2==b**2+a**2:
        print('Right Triangle')
    else:
        print('Non-Right Triangle')
'''

a=eval(input())
b=eval(input())
c=eval(input())
 
if a+b<=c or a+c<=b or b+c<=a:
    print('False')
 
else:
    print('True')
    #print(a*a+b*b)
    if a*a+b*b==c*c or a*a+c*c==b*b or c*c+b*b==a*a:
        print('Right Triangle')
    else:
        print('Non-Right Triangle')



a = int(input())
b = int(input())
c = int(input())
if a<b:
    a,b=b,a
if b<c:
    b,c=c,b
if a<b:
    a,b=b,a
 
if a<b+c:
    print("True")
    if a*a == b*b+c*c:
        print("Right Triangle")
    else:
        print("Non-Right Triangle")
else:
    print("False")



