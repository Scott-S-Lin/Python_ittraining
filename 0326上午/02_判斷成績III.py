'''
學籍 = int(input())
if 學籍 == 1:
    分數 = int(input())
    if 分數 >= 60 and 分數 <= 100:
        print('pass')
    elif 分數 >= 0 and 分數 < 60:
        print('fail')
    else:
        print('score error')
elif 學籍 == 2:
    分數 = eval(input())
    if 分數 >= 70 and 分數 <= 100:
        print('pass')
    elif 分數 >= 0 and 分數 < 70:
        print('fail')
    else:
        print('score error')#應該是score error
else:
    print('roll error')
'''


std = int(input())
if std > 2 or std < 1:
    print('roll error')
else:
    score = int(input())
    if score > 100 or score <0:
        print('score error')
    else:
        if std==1 and score>=60:
            print('pass')
        elif score>=70:
            print('pass')
        else:
            print('fail')


