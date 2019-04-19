h=eval(input())
w=eval(input())
h/=100
b=w/(h**2)

'''
A=b*10
if A%10>=5:
    b+=1
'''



print(b)

if  b<18.5:
       print("Underweight")
elif 18.5<=b<24:
        print("Normal")
elif 24<=b<27:
        print("Overweight")
elif 27<=b<30:
        print("Obese Class I ")
elif 30<=b<35:
        print("Obese Class II")
else:
    print("Obese Class III")
